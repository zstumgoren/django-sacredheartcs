import time

from ctctwspylib import CTCTConnection
from django.core.management.base import BaseCommand

from sacredheartcs.api_key import API_KEY, USER, PASSWORD
from sacredheartcs.apps.contacts.libs.loaders import load_activity, sync_bulk_contacts, fetch_bulk_contacts_export


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

        ##### GENERATE A BULK EXPORT #####
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

        # Load Bulk Export Activity
        load_activity(activity)


        #### TRY IMPORTING BULK EXPORT ####
        # retry download up to 5 times over 10 minuteS
        retries = 5
        outcome = 'failed'
        while retries > 0 and outcome == 'failed':
            activity = cnx.get_activity(activity_id)
            activity_status = activity['status']           
            if activity_status == 'COMPLETE':
                #TODO:emails = fetch_bulk_contacts_export(activity_id)
                #TODO: sync_bulk_contacts(emails)
                outcome = 'succeeded'
            else:
                retries -= 1
                time.sleep(120)

        #TODO: Log this
        print 'Data load %s for activity_id: %s' % (outcome, activity_id)
