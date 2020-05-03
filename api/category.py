from flask_restful import Resource, reqparse

from model import Category
from util.rest_resp import Resp
from . import api, db, abort_if_obj_null


@api.resource("/category/<cid>")
class CategoryResource(Resource):

    def get(self,cid):

        entity = Category.query.get(cid)

        abort_if_obj_null(entity)

        return Resp(data=entity.to_json())


    def delete(self,cid):

        entity = Category.query.get(cid)
        abort_if_obj_null(entity)

        try:
            db.session.delete(entity)
            db.session.commit()

            return Resp()
        except Exception as ex:
            db.session.rollback()

            return Resp(code=400,msg='delete error')

    def put(self,cid):
        pass


create_parse = reqparse.RequestParser()
create_parse.add_argument('name',required=True)
create_parse.add_argument('description',default='')


@api.resource("/category")
class CategoryListResource(Resource):

    def get(self):

        entices =  Category.query.all()
        data = [e.to_json() for e in entices]
        return Resp(data=data)

    def post(self):
        args = create_parse.parse_args()

        entity = Category(name=args.get('name'),description=args.get('description'))

        try:
            db.session.add(entity)
            db.session.commit()
            return Resp(data=entity.to_json())
        except Exception as ex:
            db.session.rollback()

            return Resp(code=400,msg='insert failure')