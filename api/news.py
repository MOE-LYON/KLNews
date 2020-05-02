
from flask_restful import Resource,reqparse
from . import api

from model import db, News




@api.resource(url="/news/<news_id:int>")
class NewsResource(Resource):

    def get(self,news_id):

        news =  News.query.get(news_id)

        return news.to_json()

    def put(self,news_id):
        pass

    def delete(self):
        pass

    def patch(self):
        pass


@api.resource("/news")
class NewsListResource(Resource):

    def get(self):
        pass

    def post(self):
        pass