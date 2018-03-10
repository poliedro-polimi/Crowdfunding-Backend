from __future__ import print_function

import sys, traceback
import braintreehttp
from flask import jsonify

from . import app


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
        response = jsonify({"error": {
            "type": jerr["name"],
            "message": jerr["message"]
        }})
        response.status_code = 403
    else:
        response = jsonify({"error": {
            "type": "PAYPAL_ERROR",
            "message": "There was an error processing the payment. This error has been logged and we'll try to fix it as soon as possible. In the meantime, make sure your data is correct. Contact us at info@poliedro-polimi.it"
        }})
        # https://pics.me.me/502-bad-gateway-nginx-0-7-67-502-bad-gateway-4364222.png
        response.status_code = 502

    return response


@app.errorhandler(KeyError)
@app.errorhandler(ValueError)
def handle_invalid_usage(error):
    response = jsonify({"error": "{}: {}".format(error.__class__.__name__, str(error))})
    response.status_code = 400
    return response


@app.errorhandler(Exception)
def handle_generic_exception(error):
    traceback.print_exc(file=sys.stderr)
    response = jsonify({"error": "500 Internal Server Error"})
    response.status_code = 500
    return response
