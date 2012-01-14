#!/usr/bin/env python
"""
This script syncs updates to Contacts with our backup database.
"""
import requests
from requests.auth import HTTPBasicAuth

from sacredheartcs.api_key import API_KEY, USER, PASSWORD

cc_user = '%s%%s' % (API_KEY, USER)  

# API docs for syncing Contact udpates
# http://community.constantcontact.com/t5/Documentation/Searching-for-Contacts-by-Last-Updated-Date-Synchronizing/ba-p/25053
# date must be in UTC format
# listtype must be 'active', 'remove', 'do-not-mail'

url = 'https://api.constantcontact.com/ws/customers/%(user)s/contacts?updatedsince=%(date)s&listtype=%(listtype)s'
#TODO:heuristics for last_check?
#TODO: listtype?
params = {
    'user':USER, 
    'date':last_check,
    'listtype':listtype
}

response = requests.get(url % params, auth=HTTPBasicAuth(cc_user, PASSWORD)
