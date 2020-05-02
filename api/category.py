from flask_restful import Resource
from . import api


@api.resource(urls="category/<cid>")
class CategoryResource(Resource):

    def get(self,cid):
        pass

    def delete(self,cid):
        pass

    def put(self,cid):
        pass


@api.resource(urls="category")
class CategoryListResource(Resource):

    def get(self):
        pass

    def post(self):
        pass