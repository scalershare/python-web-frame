from pecan import rest
from wsme import types as wtypes
from webdemo.api import expose
from webdemo.api.controllers.v1 import users as v1_users
import logging
logger = logging.getLogger(__name__)

class v1Controller(rest.RestController):
    users=v1_users.UsersController()

    @expose.expose(wtypes.text)
    def get(self):
        logger.info("v1Controller Method Get is called ...")
        return "python-web-frame: pecan & wsme by v1Controller"