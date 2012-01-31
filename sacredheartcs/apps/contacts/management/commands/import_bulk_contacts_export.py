import csv

from dateutil.parser import parse
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from django.template.defaultfilters import slugify

from contacts.models import Contact, ContactList, ListMembership

class Command(BaseCommand):
    args = '</path/to/bulk_export.csv>'
    help = """
    This command imports bulk exports of contacts from CC.

    REQUIRED ARGS:
      * path to file containing list of contacts who opened emails
    """

    def handle(self, *args, **options):
        contact_data = list(csv.DictReader(open(args[0],'rb')))

        # Check first row for List entries and add new lists to db.
        # List entries are prefixed with "List: ", e.g. "List: master"
        list_lkup = get_list_lkup(contact_data[0])

        # Load Contact records
        updated = 0
        for row in contact_data:
            # Create/Update contact
            payload, list_memberships = process_row(row, list_lkup)
            try:
                contact = Contact.objects.get(email_address=payload['email_address'])
                contact.__dict__.update(payload)
            except Contact.DoesNotExist:
                contact = Contact(**payload)
            contact.status = 'active'
            contact.save()
            updated += 1

            # Update Contact's List entries
            lists_added_to = 0
            for contact_list in list_memberships:
                # If Contact/List combo already exists, it will violate
                # a uniqueness constraint and raise an IntegrityError
                try:
                    membership = ListMembership(contact=contact, contact_list=contact_list)
                    membership.save()
                    lists_added_to += 1
                except IntegrityError:
                    pass
            print "Created/Updated: %s with %s lists" % (contact, lists_added_to) 

        print "Created/Updated %s Contacts" % updated


def get_list_lkup(contact_data_row):
    list_lkup = {}

    list_fields = [field for field in contact_data_row if field.startswith('List')]

    for field in list_fields:
        name = get_list_name(field)
        contact_list = ContactList.objects.get_or_create(name=name)[0]
        list_lkup[slugify(name)] = contact_list

    return list_lkup


def get_list_name(field):
    return field.split(':')[1].strip()

def process_row(row, list_lkup):
    """
    Returns kwargs dict for creating/updating a Contact record,
    along with the Contact's list memberships. The List
    memberships are a dict keyed on List name
    """
    payload = {}
    list_memberships = []

    for field, value in row.items():
        if field.startswith('List:'):
            if value == 'x':
                field_slug = slugify(get_list_name(field))
                list_memberships.append(list_lkup[field_slug])
        elif field.startswith('Custom field'):
            # db field names formatted as "custom_field1"
            custom_field = 'custom_field%s' % field.strip().split()[-1] 
            payload[custom_field]=value
        else:
            # convert "/" to '_or_' and white space to '_'
            new_field = field.replace(' ','_').replace('/','_or_').lower()
            if new_field == 'date_added':
                #datetimes formatted as '10/3/2011 8:52 AM PDT'
                value = parse(value)
            payload[new_field]=value

    return payload, list_memberships
