import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(basedir,'data.sqlite')
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'can you guess it qaq'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTFUL_JSON = {'ensure_ascii': False}