__all__ = ('DefaultConfig')

import paypalrestsdk.core


class DefaultConfig(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
    PAYPAL_CLIENT_ID = ""
    PAYPAL_CLIENT_SECRET = ""
    PAYPAL_API_URL = paypalrestsdk.core.PayPalEnvironment.SANDBOX_API_URL
    PAYPAL_WEB_URL = paypalrestsdk.core.PayPalEnvironment.SANDBOX_WEB_URL
    APP_DOMAIN = "poliedropolimi.pythonanywhere.com"
    APP_SSL = True
    APP_MODE = "development"
    APP_MAILER = "mailgun"
    APP_MAILER_FROM = ""
    APP_MAX_STRETCH_GOAL = 3
    MAILGUN_API_KEY = ""
    MAILGUN_DOMAIN = ""
    APP_ENABLE_CORS = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False