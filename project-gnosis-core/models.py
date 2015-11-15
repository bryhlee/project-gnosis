__author__ = 'Alexander S. Adranly'

'''Server side database models'''

import httplib
import endpoints
from protorpc import messages
from google.appengine.ext import ndb

class ConflictException(endpoints.ServiceException):
    """ConflictException -- exception mapped to HTTP 409 response"""
    http_status = httplib.CONFLICT

'''create an Entity model'''
class Entity(ndb.Model):
	'''initial'''
	name=ndb.StringProperty(required=True)
	description=ndb.TextProperty()