__all__ = ('pp_env', 'pp_client')

from . import app
import paypalrestsdk.core as paypal

pp_env = paypal.PayPalEnvironment(client_id=app.config["PAYPAL_CLIENT_ID"],
                                  client_secret=app.config["PAYPAL_CLIENT_SECRET"],
                                  apiUrl=app.config["PAYPAL_API_URL"],
                                  webUrl=app.config["PAYPAL_WEB_URL"])


pp_client = paypal.PayPalHttpClient(environment=pp_env)
