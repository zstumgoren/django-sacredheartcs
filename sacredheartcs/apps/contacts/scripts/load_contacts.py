#!/usr/bin/python
import csv
import sys

from django.template.defaultfilters import slugify

from contacts.models import Contact, ContactList, ListMembership
from sacredheartcs.api_key import CONSTANT_CONTACTS_API_KEY

def main():
    contact_data = list(csv.DictReader(open(sys.argv[1],'rb')))
    # Check first row for "List:" entries and add new lists to db

    list_lkup = {}
    list_fields = [field for field in contact_data[0] if field.startswith('List')]
    for field in list_fields:
        name = field.split(':')[1].strip()
        contact_list, status = ContactList.objects.get_or_create(name=name)
        list_lkup[slugify(name)] = contact_list

if __name__ == '__main__':
    main()
