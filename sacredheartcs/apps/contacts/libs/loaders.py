#!/usr/bin/env python
import csv
import sys

from dateutil.parser import parse
from requests.auth import HTTPBasicAuth
import requests 

from sacredheartcs.api_key import API_KEY, USER, PASSWORD
from sacredheartcs.apps.contacts.models import Activity


def fetch_bulk_contacts_export(activity_id):
    """
    Download bulk contacts export and returned parsed data

    REQUIRED ARG:
        Activity.cc_id (e.g. '07e5ke3u5dgy7a11on')
    """
    try:
        activity = Activity.objects.get(cc_id=activity_id)
    except Activity.DoesNotExist:
        sys.exit("\nCould not find Activity with id: %s\n" % activity_id)
    cc_user = '%'.join((API_KEY, USER))
    url = 'https://api.constantcontact.com' + activity.file_name #/ws/customers/<username>/activities/a07e5ke3u5dgy7a11on.csv
    response = requests.get(url, auth=HTTPBasicAuth(cc_user, PASSWORD))
    return csv.reader(response.content)


def load_activity(activity):
    """
    Create an Activity instance from a CC activity response dict.
    """
    def get_field_type(field):
        """
        Dynamically determine field type from model instance
        and use it to coerce data to proper type"
        """
        dj_field = activity_obj._meta.get_field_by_name(field)[0]
        field_type = dj_field.get_internal_type().lower()
        return field_type

    field_conversions = {
        'integerfield':int, 
        'datetimefield':lambda utctime:parse(utctime.split('.')[0]),
        'file_name':lambda field: field.rpartition('.')[-2],
    }

    # Initialize activity
    cc_id = activity.pop('id').split('/')[-1]
    activity_obj = Activity(cc_id=cc_id)

    # Set attributes on Activity instance
    for field, value in activity.items():
        # Account for source-to-django field name discrepancy
        field = 'activity_type' if field == 'type' else field

        field_type = get_field_type(field)

        # Convert values
        if field in field_conversions:
            try:
                value = field_conversions[field](value)
            except AttributeError:
                # If file create on CC is not complete, value will be None
                value = '' 
        elif field_type in field_conversions:
            value = field_conversions[field_type](value)
        # Default to string
        else:
            pass
        setattr(activity_obj, field, value)

    activity_obj.save()

def sync_bulk_contacts(contact_emails):
    """
    Syncs bulk export of Constant Contact emails. 

    REQUIRED ARGS:
        contact_emails - a list of cc emails
    """
    #TODO: get unique emails from db and create sets for new and deleted emails
    pass

