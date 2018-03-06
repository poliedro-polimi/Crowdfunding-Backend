import paypalrestsdk.core


class DefaultConfig(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
    PAYPAL_CLIENT_ID = ""
    PAYPAL_CLIENT_SECRET = ""
    PAYPAL_API_URL = paypalrestsdk.core.PayPalEnvironment.SANDBOX_API_URL
    PAYPAL_WEB_URL = paypalrestsdk.core.PayPalEnvironment.SANDBOX_WEB_URL
    APP_DOMAIN = "poliedropolimi.pythonanywhere.com"
    APP_SSL = True
    APP_WEB_ROOT = ""
    APP_MODE = "development"