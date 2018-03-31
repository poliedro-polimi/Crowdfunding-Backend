import base64

import requests, time

from . import app

# import paypalrestsdk.core as paypal

pp_env = paypal.PayPalEnvironment(client_id=app.config["PAYPAL_CLIENT_ID"],
                                  client_secret=app.config["PAYPAL_CLIENT_SECRET"],
                                  apiUrl=app.config["PAYPAL_API_URL"],
                                  webUrl=app.config["PAYPAL_WEB_URL"])

pp_client = paypal.PayPalHttpClient(environment=pp_env)


class AccessToken(object):

    def __init__(self, access_token, expires_in, token_type):
        self.access_token = access_token
        self.expires_in = expires_in
        self.token_type = token_type
        self.created_at = time.time()

    def is_expired(self):
        return self.created_at + self.expires_in <= time.time()

    def authorization_string(self):
        return "{0} {1}".format(self.token_type, self.access_token)


class PayPalAPI(object):
    def __init__(self, client_id, client_secret, api_url, web_url):
        self.client_id = client_id
        self.client_secret = client_secret
        self.api_url = api_url
        self.web_url = web_url

    def payment_create_request(self, body):
        # r = requests.post

        self.verb = "POST"
        self.path = "/v1/payments/payment?"
        self.headers = {}
        self.headers["Content-Type"] = "application/json"

    def get_token_request(self, refresh_token=None):
        path = "/v1/oauth2/token"
        verb = "POST"
        body = {}
        if refresh_token:
            body['grant_type'] = 'refresh_token'
            body['refresh_token'] = refresh_token
        else:
            body['grant_type'] = 'client_credentials'

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": self.auth_string
        }

        resp = requests.post(url=self.base_url + path, headers=headers,
                json=data)

    @property
    def auth_string(self):
        return "Basic {0}".format(base64.b64encode((self.client_id + ":" + self.client_secret).encode()).decode())
