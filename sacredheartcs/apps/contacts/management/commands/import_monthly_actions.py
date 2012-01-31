import csv

from django.core.management.base import BaseCommand
from dateutil.parser import parse

from sacredheartcs.apps.contacts.models import Contact, EmailAction

class Command(BaseCommand):
    args = '</path/to/monthly_openers/YYYY_April_readers.csv> YYYY-MM-DD'
    help = """
    This script performs bulk inserts of responses to email outreach campaigns. 
    It requires a bulk list of contacts who opened an outreach email in a certain month.

    These lists of contacts are exported from Constant Contacts.

    REQUIRED ARGS:
      * path to file containing list of contacts who opened emails
      * date to associate with the action
    """

    def handle(self, *args, **options):

        action_date = parse(args[1])

        # Fetch Contact records for unique set of emails from input file
        contacts = list(csv.reader(open(args[0],'rb')))

        # Create dictionary of unique contacts
        unique_contacts = {}
        for contact in contacts[1:]: # Skip header row 
            email = contact[0].strip()
            unique_contacts[email]=contact

        # Fetch/Create Contact record and insert Opened action
        action = 'opened' 
        for email, contact in unique_contacts.items():
            try:
                contact = Contact.objects.get(email_address=email)
            except Contact.DoesNotExist:
                contact = Contact.objects.create(email_address=email,
                                                 first_name=contact[1],
                                                 last_name=contact[2],
                                                 company_name=contact[3])
                print "Created Contact record for %s" % email

            EmailAction.objects.get_or_create(contact=contact,
                                              action=action,
                                              action_date=action_date)

            print "%s marked as having %s a %s email" % (email, action, action_date)
