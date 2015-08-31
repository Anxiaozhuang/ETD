#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""createNewCollection.py: Creates a new collection in the ETD service."""

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

# The ID of the database
db_id = 'test_db'

# The ID of the collection in the database
coll_id = 'test_coll'

req = urllib2.Request(apiURL + 'etd/v1.0/database/' + db_id  + '/collection', headers={"Content-Type": "application/json"}, data = coll_id)
resp = urllib2.urlopen(req)
response = json.loads(resp.read())
print response	