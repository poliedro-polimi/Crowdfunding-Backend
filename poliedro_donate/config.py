__all__ = ('DefaultConfig')

import paypalrestsdk.core


class DefaultConfig(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
    PAYPAL_CLIENT_ID = ""
    PAYPAL_CLIENT_SECRET = ""
    PAYPAL_API_URL = paypalrestsdk.core.PayPalEnvironment.SANDBOX_API_URL
    PAYPAL_WEB_URL = paypalrestsdk.core.PayPalEnvironment.SANDBOX_WEB_URL
    PAYPAL_WEB_EXPERIENCE_PROFILE_ID = None
    APP_DOMAIN = "poliedropolimi.pythonanywhere.com"
    APP_SSL = True
    APP_SSL_AGE = 300
    APP_MODE = "development"
    APP_MAILER = "mailgun"
    APP_MAILER_FROM = ""
    APP_MAX_STRETCH_GOAL = 3
    APP_SG_COSTS = {
        0: 0,
        1: 1,
        2: 2,
        3: 3
    }
    PAYPAL_FIXED_FEE = 0.35
    PAYPAL_FEE = 3.4/100
    MAILGUN_API_KEY = ""
    MAILGUN_DOMAIN = ""
    APP_ENABLE_CORS = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False