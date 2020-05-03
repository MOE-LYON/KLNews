from flask import Blueprint
from flask_restful import Api, abort

api_bp = Blueprint(name='api', import_name=__name__,url_prefix='/api')
from .file import *

api = Api(prefix="/api")


def abort_if_obj_null(obj, msg="you request resource is  not exist"):
    if obj is None:
        abort(404, message=msg)


from .news import *
from .category import *
