from __future__ import print_function

import sys, traceback, json
import braintreehttp
from flask import jsonify

from . import app


class DonationError(Exception):
    def __init__(self, donation, parent_exc=None):
        self.donation = donation
        self.parent_exc = parent_exc
        self.donation_id = donation.pretty_id

        if parent_exc:
            parent_exc.donation_id = self.donation_id

        super(DonationError, self).__init__("Donation ID: {}".format(self.donation_id))


@app.errorhandler(braintreehttp.HttpError)
def handle_paypal_error(error):
    print("\n---- PayPal error ----", file=sys.stderr)
    print(error.status_code, file=sys.stderr)
    print(error.headers["PayPal-Debug-Id"], file=sys.stderr)
    print(error.message, file=sys.stderr)

    body = getattr(error, "body", None)

    if body:
        print("--- Request body ----", file=sys.stderr)
        print(body, file=sys.stderr)

    print("----------------------\n", file=sys.stderr)

    jerr = json.loads(error.message)

    if error.status_code == 403:
        ejson = {"error": {
                "type": jerr["name"],
                "message": jerr["message"]
            }}
    else:
        ejson = {"error": {
            "type": "_PAYPAL_ERROR",
            "message": "There was an error processing the payment. This error has been logged and we'll try to fix it as soon as possible. In the meantime, make sure your data is correct. Please submit an issue at https://github.com/poliedro-polimi/Crowdfunding-Backend/issues"
        }}

    if getattr(error, "donation_id", None):
        ejson["error"]["donation_id"] = error.donation_id

    response = jsonify(ejson)

    if error.status_code == 403:
        response.status_code = 403
    else:
        # https://pics.me.me/502-bad-gateway-nginx-0-7-67-502-bad-gateway-4364222.png
        response.status_code = 502

    return response


@app.errorhandler(DonationError)
def handle_donation_error(error):
    # Log entire traceback, including the DonationError
    app.log_exception(sys.exc_info())

    # Find handler for parent exception and call it
    # noinspection PyProtectedMember
    return app._find_error_handler(error.parent_exc)(error.parent_exc)


@app.errorhandler(KeyError)
@app.errorhandler(ValueError)
def handle_invalid_usage(error):
    ejson = {"error": {
        "type": "_VALIDATION_ERROR",
        "message": "{}: {}".format(error.__class__.__name__, str(error))
    }}

    if getattr(error, "edesc", None):
        ejson["error"]["desc"] = error.edesc

    if getattr(error, "donation_id", None):
        ejson["error"]["donation_id"] = error.donation_id

    response = jsonify(ejson)
    response.status_code = 400
    return response


@app.errorhandler(Exception)
def handle_generic_exception(error):
    traceback.print_exc(file=sys.stderr)
    ejson = {"error": {
        "type": "_APP_ERROR",
        "message": "500 Internal Server Error"}
    }

    if getattr(error, "donation_id", None):
        ejson["error"]["donation_id"] = error.donation_id

    response = jsonify(ejson)
    response.status_code = 500
    return response
