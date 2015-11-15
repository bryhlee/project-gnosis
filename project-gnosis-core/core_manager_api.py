"""
Main Function
"""
import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote
from models import ConflictException
from models   import Entity
from google.appengine.ext import ndb


package = 'Package'


class Package(messages.Message):
    """String that stores a message."""
    greeting = messages.StringField(1)

@endpoints.api(name='gcore-endpoints', version='v1')
class HelloWorldApi(remote.Service):
    """GnosisCore API v1."""


   	@endpoints.method(message_types.VoidMessage, Package,
        path = "displayAllEntities", http_method='GET', name="displayAllEntities")
    def show_people(self,request):

      text="All Queries:\n"
      q= Entity.query()
      
      for e in q:
        text+= e.name
        text+= " , "
        text+= e.description
        text+="\n"

      return Package(greeting=text)



APPLICATION = endpoints.api_server([GCoreApi])
'''was originally HelloWorldApi'''