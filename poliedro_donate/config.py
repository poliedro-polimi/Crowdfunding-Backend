import paypalrestsdk.core


class DefaultConfig(object):
    SUPPORTED_LANGUAGES =  {'it': 'Italiano', 'en': 'English'}
    BABEL_DEFAULT_LOCALE = 'it'
    BABEL_DEFAULT_TIMEZONE = 'Europe/Rome'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
    PAYPAL_CLIENT_ID = ""
    PAYPAL_CLIENT_SECRET = ""
    PAYPAL_API_URL = paypalrestsdk.core.PayPalEnvironment.SANDBOX_API_URL,
    PAYPAL_WEB_URL = paypalrestsdk.core.PayPalEnvironment.SANDBOX_WEB_URL,
    APP_DOMAIN = "poliedropolimi.pythonanywhere.com"
    APP_SSL = True
    APP_WEB_ROOT = ""