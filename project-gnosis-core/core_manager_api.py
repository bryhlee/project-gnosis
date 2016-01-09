"""
Main Function
"""
import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote
from models import ConflictException
from models   import Api
from google.appengine.ext import ndb


REQUEST_ENTITY_CONTAINER = endpoints.ResourceContainer(
    name=messages.StringField(1),
    description=messages.StringField(2),
    dl_link=messages.StringField(3),
    doc_link=messages.StringField(4),
)

REQUEST_ENTITY_LIST_CONTAINER = endpoints.ResourceContainer(
    entity_list = messages.StringField(1)
)


package = 'Package'

class Package(messages.Message):
    """String that stores a message."""
    display_msg = messages.StringField(1)

@endpoints.api(name='gnosis_endpoints', version='v1')
class GCoreApi(remote.Service):

    """GnosisCore API v1."""

    @endpoints.method(REQUEST_ENTITY_CONTAINER, Package, 
        path = "update", http_method='GET', name="update")
    def submit_update(self,request):
        text=""
        q=Api.query()
        q1 = q.filter(Api.name == request.name)
        api = q1.get()

        if api is not None:
            api.description = request.description
            api.download = request.dl_link
            api.documentation = request.doc_link
            text= "Updating: \n\n"
        else:
            api = Api(name=request.name,description=request.description,download=request.dl_link,documentation=request.doc_link)
            text= "Creating: \n\n"

        api.put()
        text= text + request.name+"\n"+request.description+"\n"+request.dl_link+"\n"+request.doc_link

        return Package(display_msg=text)


    @endpoints.method(REQUEST_ENTITY_LIST_CONTAINER, Package,
        path = "deleteEntities", http_method='GET', name="deleteEntities")
    def delete_entity(self,request):
        raw_msg = request.entity_list
        msg_group = raw_msg.split('*')
        
        for i in range(len(msg_group)-1):
            q = Api.query(Api.name == msg_group[i])
            e = q.get()
            e.key.delete()

        return Package(display_msg=raw_msg)

    @endpoints.method(message_types.VoidMessage, Package,
        path = "getEntities", http_method='GET', name="getEntities")
    def retrieve_entities(self, request):
        text=""
        q= Api.query()

        for e in q:
          text+= (e.name + "*" + e.description + "*" + e.download + "*" + e.documentation + "*\n")

        return Package(display_msg=text)


APPLICATION = endpoints.api_server([GCoreApi])
'''was originally HelloWorldApi'''