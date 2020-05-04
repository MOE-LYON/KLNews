from flask import Flask

from config.config import Config
from model import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # blueprint register
    from api import api_bp
    app.register_blueprint(api_bp)

    from api import api
    api.init_app(app)


    return app

app = create_app()
if __name__ == '__main__':

    app.run()
