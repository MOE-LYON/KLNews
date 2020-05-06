from flask_restful import Resource, reqparse

from util.rest_resp import Resp
from . import api, abort_if_obj_null

from model import db, News


@api.resource("/news/<news_id>")
class NewsResource(Resource):

    def get(self, news_id):

        news = News.query.get(news_id)
        abort_if_obj_null(news)

        return Resp(data=news.to_json())

    def put(self, news_id):
        args = create_parse.parse_args()

        news = News.query.get(news_id)
        abort_if_obj_null(news)
        args['body'] = args.pop("content")
        args['category_id'] = args.pop("cid")
        for prop in args:
            if args.get(prop):
                setattr(news,prop,args.get(prop))
        db.session.commit()

        return Resp(data=news.to_json())

    def delete(self, news_id):

        news = News.query.get(news_id)
        abort_if_obj_null(news)

        try:
            db.session.delete(news)
            db.session.commit()
            return Resp()
        except Exception as ex:
            db.session.rollback()
            print(ex.args.__str__())
            return Resp(code=400, msg='delete error')

    def patch(self,news_id):
        pass


news_parse = reqparse.RequestParser()

news_parse.add_argument("page", type=int, default=1,location='args')
news_parse.add_argument('pagesize', type=int, default=12,location='args')
news_parse.add_argument('keyword', type=str, default='',location='args')
news_parse.add_argument('cid', type=int, default=0,location='args')


create_parse = reqparse.RequestParser()
create_parse.add_argument("cid",type=int,required=True)
create_parse.add_argument("title",type=str,required=True)
create_parse.add_argument('content',type=str,required=True)
create_parse.add_argument('front_image',required=True)


@api.resource("/news")
class NewsListResource(Resource):

    def get(self):
        args = news_parse.parse_args()
        temp_query = News.query.filter(News.title.like("%" + args.get('keyword') + "%"))
        if args.get('cid'):
            temp_query = temp_query.filter(News.category_id==args.get('cid'))
        pagination = temp_query.paginate(args.get('page'),args.get('pagesize'),error_out=False)
        data = {
            'totalpage':pagination.pages,
            'items' :[ item.to_json() for item in pagination.items],
            'page':pagination.page,
            'pagesize':pagination.per_page
        }
        return Resp(data=data)

    def post(self):

        args = create_parse.parse_args()

        news = News(
            category_id=args.get('cid'),
            title=args.get('title'),
            body=args.get('body'),
            front_image=args.get('front_image'),
        )

        try:
            db.session.add(news)
            db.session.commit()

            return Resp(data=news.to_json())
        except Exception as ex:
            db.session.rollback()
            return Resp(code=400,msg='create news error')
