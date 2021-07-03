from os import environ
from flask_cors import CORS
from flask.app import Flask
from flask_wtf import CSRFProtect
from flask_restful import Api

config = {
    'test': 'TEST_DATABASE_URI',
    'dev': 'DEV_DATABASE_URI'
}

def setup_config(cfg_name: str):
    environ['SQLALCHEMY_DATABASE_URI'] = environ.get(config[cfg_name])
    
    app = Flask(__name__)
    if environ.get('ENABLE_CSRF') == 1:
        app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
        app.config['WTF_CSRF_SECRET_KEY'] = environ.get('WTF_CSRF_SECRET_KEY')
        csrf = CSRFProtect()
        csrf.init_app(app)
        
    CORS(app, resources={r"/*": {"origins": "http://localhost:3000", "send_wildcard": "False"}})
    api = Api(app)


    # This import must be postponed because importing common.database has side-effects
    from common.database import init_db
    init_db()


    # This import must be postponed after init_db has been called
    from controller.hashtag_controller import HashtagResource
    api.add_resource(HashtagResource, '/api/<value>')


    # This import must be postponed after init_db has been called
    from models.models import PostTag, Post, Tag, User
    if cfg_name == 'test':
        PostTag.query.delete()
        Post.query.delete()
        Tag.query.delete()
        User.query.delete()

    return app
