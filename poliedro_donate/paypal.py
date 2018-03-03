from . import app
import paypalrestsdk.core as paypal
import paypalrestsdk.v1.payments as payments

pp_env = paypal.PayPalEnvironment(client_id=app.config["PAYPAL_CLIENT_ID"],
                               client_secret=app.config["PAYPAL_CLIENT_SECRET"],
                               mode=app.config["PAYPAL_MODE"])

pp_client = payments.PayPalHttpClient(environment=pp_env)
