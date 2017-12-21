class DefaultConfig(object):
    SUPPORTED_LANGUAGES =  {'it': 'Italiano', 'en': 'English'}
    BABEL_DEFAULT_LOCALE = 'it'
    BABEL_DEFAULT_TIMEZONE = 'Europe/Rome'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'