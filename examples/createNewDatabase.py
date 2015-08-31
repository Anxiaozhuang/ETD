#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""createNewDatabase.py: Creates a new database in the ETD service."""

__author__ = "Filip Lemic"
__copyright__ = "Copyright 2015, Telecommunciation Networks Group (TKN), TU Berlin"

__version__ = "1.0.0"
__maintainer__ = "Filip Lemic"
__email__ = "lemic@tkn.tu-berlin.de"
__status__ = "Development"

import sys
import urllib2
import json

# The URL where server listens
apiURL = 'http://localhost:5000/'

# Database name 
db_id = 'test_db'

req = urllib2.Request(apiURL + 'etd/v1.0/database', headers={"Content-Type": "application/json"}, data = db_id)
resp = urllib2.urlopen(req)
response = json.loads(resp.read())
print response	