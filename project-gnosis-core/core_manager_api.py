"""
Main Function
"""
import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote
from models import ConflictException
from models   import Person
from google.appengine.ext import ndb


package = 'Package'


class Package(messages.Message):
    """String that stores a message."""
    greeting = messages.StringField(1)

@endpoints.api(name='gcore-endpoints', version='v1')
class HelloWorldApi(remote.Service):
    """GnosisCore API v1."""



APPLICATION = endpoints.api_server([HelloWorldApi])