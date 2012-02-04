import csv
import time

from ctctwspylib import CTCTConnection
from dateutil.parser import parse
from django.core.management.base import BaseCommand
from requests.auth import HTTPBasicAuth
import requests 

from sacredheartcs.api_key import API_KEY, USER, PASSWORD

from contacts.models import Activity



def load_csv_export(activity_id):
    """
    For a given Export activity, fetches
    the download and attempts to load data
    """
    try:
        activity = Activity.objects.get(cc_id=activity_id)
    except Activity.DoesNotExist:
        print "Could not find Activity with id: %s" % activity_id
        activity = None

    if activity:
        # Get file name and fetch remote resource
        cc_user = '%'.join((API_KEY, USER))
        url = 'https://api.constantcontact.com' + activity.file_name #/ws/customers/<username>/activities/a07e5ke3u5dgy7a11on.csv
        response = requests.get(url, auth=HTTPBasicAuth(cc_user, PASSWORD))
        data = csv.reader(response.content)
        #TODO: get unique emails from db and create sets for new and deleted emails


def load_activity(activity):
    """
    Create an Activity instance from a CC activity response dict.
    """

    field_conversions = {'integer':int, 'datetime':parse}

    # Initialize activity
    activity_obj = Activity(cc_id=activity.pop('id'))

    for field, value in activity.items():
        # Dynamically determine field type and use it to coerce data to proper type
        dj_field = activity_obj._meta.get_field_by_name(field)[0]
        field_type = dj_field.get_internal_type().split('Field')[0].lower()
        try:
            func = field_conversions[field_type]
            value = func(value)
        except KeyError:
            # Default to string
            pass
        setattr(activity_obj, field, value)


class Command(BaseCommand):

    help = """
    Syncs the db with active contacts on Constant Contacts.
    New contacts are added to the database; contacts in the
    db but no longer on CC's Active list will be archived.

    Below are individual steps triggered by this command:

    * Generate a Bulk Export Activity (on CC) for all Active contacts
    * Add an Export entry to the Activity model
    * Wait (up to 10 minutes) for the CSV download to be ready
    * If download is ready, fetch it and load data

    """

    def handle(self, *args, **options):
        # Set up CC connection
        cnx = CTCTConnection(API_KEY, USER, PASSWORD)

        # GENERATE EXPORT ACTIVITY FOR ACTIVE CONTACTS
        active_list_uri = 'http://api.constantcontact.com/ws/%s/lists/active' % USER

        # Create an export activity as a csv file
        activity_uri = cnx.create_activity(type='EXPORT_CONTACTS',
                                           lists=[active_list_uri],
                                           data={'fileType':'TXT'})

        activity_id = activity_uri.rpartition('/')[-1]

        # Check the activity status
        activity = cnx.get_activity(activity_id)

        # Load export into Activity model
        load_activity(activity)

        # RETRY FILE DOWNLOAD FOR UP TO 10 MINUTES
        retries = 5
        outcome = 'failed'
        while retries > 0:
            activity = cnx.get_activity(activity_id)
            activity_status = activity['status']

            if activity_status == 'COMPLETE':
                outcome = 'succeeded'
                #load_csv_export(activity_id)
                break
            else:
                retries -= 1
                time.sleep(120)

        #TODO: Log this
        print 'data load %s for activity_id: %s' % (outcome, activity_id)
