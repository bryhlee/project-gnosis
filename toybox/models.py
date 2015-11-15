__author__ = 'Alexander S. Adranly'

'''Server side database models'''

import httplib
import endpoints
from protorpc import messages
from google.appengine.ext import ndb

class ConflictException(endpoints.ServiceException):
    """ConflictException -- exception mapped to HTTP 409 response"""
    http_status = httplib.CONFLICT

class Person(ndb.Model):
	"""Person -- Person object"""
	name=ndb.StringProperty(required=True)
	age=ndb.StringProperty(required=True)

		