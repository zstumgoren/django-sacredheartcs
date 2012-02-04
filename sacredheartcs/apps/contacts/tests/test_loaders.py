import datetime

from django.test import TestCase

from sacredheartcs.apps.contacts.libs import loaders
from sacredheartcs.apps.contacts.models import Activity


class TestDataLoad(TestCase):

    def setUp(self):

        self.activities_data = [
            {'errors': '0',
              'file_name': None,
              'id': 'http://api.constantcontact.com/ws/customers/username/activities/a07e5ke3u5dgy7a11on',
              'insert_time': '2012-02-03T13:55:33.191Z',
              'run_finish_time': '2012-02-03T13:57:52.801Z',
              'run_start_time': '2012-02-03T13:56:12.566Z',
              'status': 'COMPLETE',
              'transaction_count': '15578',
              'type': 'EXPORT_CONTACTS',
              'updated': '2012-02-03T13:57:52.801Z'},
             {'errors': '5',
              'file_name': None,
              'id': 'http://api.constantcontact.com/ws/customers/username/activities/a07e59vxt4mgutvhlp4',
              'insert_time': '2011-11-10T14:48:24.088Z',
              'run_finish_time': '2011-11-10T14:48:44.654Z',
              'run_start_time': '2011-11-10T14:48:43.740Z',
              'status': 'COMPLETE',
              'transaction_count': '12',
              'type': 'ADD_CONTACT_DETAIL',
              'updated': '2011-11-10T14:48:44.654Z'},
        ]

    def test_load_activities(self):
        loaders.load_activity(self.activities_data[0])
        activity = Activity.objects.all()[0]
        self.assertEqual(activity.cc_id, 'a07e5ke3u5dgy7a11on')
        self.assertEqual(activity.errors, 0)
        self.assertEqual(activity.insert_time, datetime.datetime(2012, 2, 3, 13,55, 33))
        self.assertEqual(activity.run_start_time, datetime.datetime(2012, 2, 3, 13, 56, 12))
        self.assertEqual(activity.run_finish_time, datetime.datetime(2012, 2, 3, 13, 57, 52))
        self.assertEqual(activity.status, 'COMPLETE')
        self.assertEqual(activity.transaction_count, 15578)
        self.assertEqual(activity.activity_type, 'EXPORT_CONTACTS')
        self.assertEqual(activity.updated, datetime.datetime(2012, 2, 3, 13, 57, 52))
        self.assertEqual(activity.synced, False)


class TestLoadCSVExport(TestCase):

    def setUp(self):
        Activity.objects.create(
            cc_id='a07e5ke3u5dgy7a11on',
            errors=0,
            insert_time=datetime.datetime(2012, 2, 3, 13,55, 33),
            run_start_time=datetime.datetime(2012, 2, 3, 13, 56, 12),
            run_finish_time=datetime.datetime(2012, 2, 3, 13, 57, 52),
            status='COMPLETE',
            transaction_count=15578,
            activity_type='EXPORT_CONTACTS',
            updated=datetime.datetime(2012, 2, 3, 13, 57, 52),
            synced=False)
    
    def test_sync_bulk_contacts(self, *args):
        #TODO:test email synchronization and Activity.synced flag
        emails = ['foo@gmail.com', 'baz@gmail.com'] 
        loaders.sync_bulk_contacts(emails)
        #Contact.objects.filter(email_address='foo@gmail.com')

