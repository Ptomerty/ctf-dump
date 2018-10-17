#!/usr/bin/env python

import hashlib
import requests



import urllib2
"""
read old length from file into variable
"""
request = urllib2.Request('http://www.yahoo.com')
request.get_method = lambda : 'HEAD'

response = urllib2.urlopen(request)
new_length = response.info()["Content-Length"]
if old_length != new_length:
    print "something has changed"