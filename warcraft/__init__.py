
import logging
import os

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_pagedown import PageDown
from flask_babel import Babel

from . import config

APP_DIR = os.path.dirname(__file__)
CONFIG_MODULE = os.environ.get('WARCRAFT_CONFIG', 'default')

bootstrap = Bootstrap()
mail = Mail()
db = SQLAlchemy()
moment = Moment()
pagedown = PageDown()
babel = Babel()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    #app config
    appconfig = config.config[CONFIG_MODULE]
    app.config.from_object(appconfig)
    appconfig.init_app(app)
    app.config.from_pyfile('application.cfg', silent=True)

    #flask ext
    bootstrap.init_app(app)
    
    mail.init_app(app)
    db.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)
    pagedown.init_app(app)
    babel.init_app(app)

    #regist blueprint
    from .main import main as main_blueprint 
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    return app
