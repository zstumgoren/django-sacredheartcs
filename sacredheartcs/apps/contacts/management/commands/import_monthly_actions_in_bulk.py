import csv

from django.db.utils import IntegrityError
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


        incoming_contacts = list(csv.reader(open(args[0],'rb')))

        # Create mapping of emails to incoming contact info (skipping the header line)
        cc_contacts_lkup = dict([(contact[0], contact) 
                                 for contact in incoming_contacts[1:]])
        
        # Create mapping of emails to Contact instances
        db_contacts_lkup = dict([(contact.email_address, contact) 
                                 for contact in Contact.objects.all()])

        # Find contacts not yet in db
        new_emails = set(cc_contacts_lkup.keys()) - set(db_contacts_lkup.keys())

        # STEP 1: Bulk insert new contacts
        new_contacts = []
        for email in new_emails:
            contact = cc_contacts_lkup[email]
            contact_obj = Contact(email_address=email,
                                  first_name=contact[1],
                                  last_name=contact[2],
                                  company_name=contact[3],
                                  needs_update=True)
            new_contacts.append(contact_obj)

            # Update db_contacts lookup with new instance
            #db_contacts_lkup[email] = contact_obj

        Contact.objects.bulk_create(new_contacts)
        print "Bulk created %s new Contact records" % len(new_contacts)

        # Refresh our mapping of emails to Contact instances, which 
        # should now include newly imported contacts
        db_contacts_lkup = dict([(contact.email_address, contact) 
                                 for contact in Contact.objects.all()])

        # STEP 2: Bulk load EmailActions
        action = 'opened' 
        action_date = parse(args[1])
        email_actions = []
        for email in cc_contacts_lkup:
            contact = db_contacts_lkup[email]
            email_actions.append(EmailAction(contact_id=contact.id,
                                             action=action,
                                             action_date=action_date))
        try:
            EmailAction.objects.bulk_create(email_actions)
            print "Bulk created %s new EmailActions for %s" % (len(email_actions), action_date)
        except IntegrityError, e:
            print IntegrityError(e[0] + "Are you trying to import previously loaded Email Actions?")
                             
