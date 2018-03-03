import paypalrestsdk


class DefaultConfig(object):
    SUPPORTED_LANGUAGES =  {'it': 'Italiano', 'en': 'English'}
    BABEL_DEFAULT_LOCALE = 'it'
    BABEL_DEFAULT_TIMEZONE = 'Europe/Rome'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
    PAYPAL_CLIENT_ID = ""
    PAYPAL_CLIENT_SECRET = ""
    PAYPAL_MODE = paypalrestsdk.PayPalEnvironment.SANDBOX
    APP_DOMAIN = "support-api.poliedro-polimi.it"
    APP_SSL = True
    APP_WEB_ROOT = ""