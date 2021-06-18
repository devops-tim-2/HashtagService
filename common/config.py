from os import environ
from typing import Tuple
from flask_cors import CORS
from flask.app import Flask
from flask_sqlalchemy import SQLAlchemy
from common.database import db
from models.post_tag import PostTag
from models.post import Post
from models.tag import Tag
from models.user import User


DevConfig = {
    'DEBUG': True,
    'DEVELOPMENT': True,
    'SQLALCHEMY_DATABASE_URI': f'{environ.get("DB_TYPE")}+{environ.get("DB_DRIVER")}://{environ.get("DB_USER")}:{environ.get("DB_PASSWORD")}@{environ.get("DB_HOST")}/{environ.get("DB_NAME")}',
    'SQLALCHEMY_ECHO': True,
    'SQLALCHEMY_TRACK_MODIFICATIONS': False
}


ProdConfig = {}


TestConfig = {
    'DEBUG': False,
    'DEVELOPMENT': True,
    'SQLALCHEMY_DATABASE_URI': f'{environ.get("TEST_DATABASE_URI")}',
    'SQLALCHEMY_ECHO': True,
    'SQLALCHEMY_TRACK_MODIFICATIONS': False
}


config: dict = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'test': TestConfig
}


def setup_config(cfg_name: str) -> Tuple[Flask, SQLAlchemy]:
    app = Flask(__name__)
    CORS(app)
    # app.register_blueprint(product_api, url_prefix='/api/product')
    # app.register_blueprint(order_api, url_prefix='/api/order')
    # app.register_blueprint(report_api, url_prefix='/api/report')
    # app.register_blueprint(user_api)

    cfg = config.get(cfg_name)
    for key in cfg.keys():
        app.config[key] = cfg[key]

    app.app_context().push()
    db.init_app(app)

    with app.app_context():
        db.create_all()

    if cfg_name == 'test':
        PostTag.query.delete()
        Post.query.delete()
        Tag.query.delete()
        User.query.delete()

    return app, db
