import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    # ---------------------------------------------------------
    # WarCraft specifix config
    # ---------------------------------------------------------
    WEBSERVER_THREADS = 8

    WARCRAFT_WEBSERVER_PORT = 5050
    WARCRAFT_WEBSERVER_TIMEOUT = 60

    # Your App secret key
    SECRET_KEY = '\2\1thisismyscretkey\1\2\e\y\y\h'  # noqa

    # Flask-WTF flag for CSRF
    CSRF_ENABLED = True

    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    #Mail
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    WARCRAFT_MAIL_SUBJECT_PREFIX = '[WarCraft]'
    WARCRAFT_MAIL_SENDER = 'WarCraft Admin <flasky@example.com>'
    WARCRAFT_ADMIN = os.environ.get('WARCRAFT_ADMIN')

    # ---------------------------------------------------
    # Babel config for translations
    # ---------------------------------------------------
    # Setup default language
    BABEL_DEFAULT_LOCALE = 'en'
    # Your application default translation path
    BABEL_DEFAULT_FOLDER = 'babel/translations'
    # The allowed translation for you app
    LANGUAGES = {
        'en': {'flag': 'us', 'name': 'English'},
        'zh': {'flag': 'cn', 'name': 'Chinese'},
    }

    #----
    APP_NAME = "WarCraft"

    WARCRAFT_POSTS_PER_PAGE = 10

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(BASE_DIR, 'data-dev.sqlite')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite:///' + os.path.join(BASE_DIR, 'data-test.sqlite')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(BASE_DIR, 'data.sqlite')

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

