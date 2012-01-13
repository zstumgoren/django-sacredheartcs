#!/usr/bin/python
import csv
import datetime
import re
import sys

from django.template.defaultfilters import slugify

from contacts.models import Contact, ContactList, ListMembership
from sacredheartcs.api_key import CONSTANT_CONTACTS_API_KEY

def main():
    contact_data = list(csv.DictReader(open(sys.argv[1],'rb')))
    # Check first row for List entries and add new lists to db
    # list entries are prefixed with "List: ", e.g. "List: master" 

    list_lkup = {}
    list_fields = [field for field in contact_data[0] if field.startswith('List')]
    for field in list_fields:
        name = field.split(':')[1].strip()
        contact_list = ContactList.objects.get_or_create(name=name)[0]
        list_lkup[slugify(name)] = contact_list
    
    # regex for skipping fields
    fields_to_skip = re.compile(r'(List:|Custom field)')
    # Load Contact records
    for row in contact_data:
        payload = {}
        for field, value in row.items():
            # Skip List and Custom fields"
            if not re.match(fields_to_skip, field):
                # convert "/" to '_or_' and white space to '_'
                new_field = field.replace(' ','_').replace('/','_or_').lower()
                if new_field == 'date_added':
                    #TODO: format date '10/3/2011 8:52 AM PDT'
                    value = datetime.datetime.strptime('%m/%d/%Y %H:%S %p %Z', value)
                    print value
                    break
                payload[new_field]=value

        # Create contact
        contact = Contact.objects.get(email_address=payload['email_address'])
        if contact:
            contact.__dict__.update(payload)
        else:
            contact = Contact(**payload)
        contact.save()

        #TODO: Update contacts List entries

        

if __name__ == '__main__':
    main()
