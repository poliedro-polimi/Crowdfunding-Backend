from __future__ import print_function
from __future__ import print_function

import sys
import traceback

import braintreehttp
from flask import request, jsonify, url_for
from werkzeug.exceptions import InternalServerError

from poliedro_donate import strings
from .utils import validate_donation_request, validate_execute_request
from . import app
from .paypal import pp_client

import paypalrestsdk.v1.payments as payments

@app.errorhandler(KeyError)
@app.errorhandler(ValueError)
def handle_invalid_usage(error):
    response = jsonify({"error": "{}: {}".format(error.__class__.__name__, str(error))})
    response.status_code = 400
    return response

@app.route(app.config["APP_WEB_ROOT"] + '/paypal/create', methods=('POST',))
def paypal_create_payment():
    req = request.get_json()

    try:
        validate_donation_request(req)
    except Exception:
        traceback.print_exc(file=sys.stderr)
        raise

    lang = req["lang"]

    if int(request.args.get("validate_only", 0)) and app.config["APP_MODE"] == "development":
        return jsonify({"success": "Provided JSON looks good"})

    payment_create_request = payments.PaymentCreateRequest()
    payment_create_request.request_body({
        "payer": {
            "payment_method": "paypal"
        },
        "intent": "sale",
        "transactions": [{
            "amount": {
                "total": str(req["donation"]),
                "currency": "EUR"
            },
            "item_list": {
                "items": [
                    {
                        "quantity": "1",
                        "name": strings.PP_ITEM_NAME[lang],
                        "price": str(req["donation"]),
                        "currency": "EUR",
                        "description": strings.PP_ITEM_DESC(lang, req["stretch_goal"], req["items"]),
                        "tax": "1"
                    },
                ]
            }
        }],
        "redirect_urls": {
            "cancel_url": url_for("paypal_cancel"),
            "return_url": url_for("paypal_return")
        },
        "description": strings.PP_ITEM_NAME[lang]
    })

    try:
        payment_create_response = pp_client.execute(payment_create_request)
        payment = payment_create_response.result
    except IOError as ioe:
        if isinstance(ioe, braintreehttp.HttpError):
            # Something went wrong server-side
            print("Server error", file=sys.stderr)
            print(ioe.status_code, file=sys.stderr)
            print(ioe.headers["PayPal-Debug-Id"], file=sys.stderr)
        else:
            # Something went wrong client side
            traceback.print_exc()
        raise InternalServerError(jsonify({"error": "Server error"}))

    return jsonify({"paymentID": payment.id})


@app.route(app.config["APP_WEB_ROOT"] + '/paypal/execute')
def paypal_execute():
    req = request.json

    try:
        validate_execute_request(req)
    except Exception:
        traceback.print_exc(file=sys.stderr)
        raise

    if int(request.args.get("validate_only", 0)) and app.config["APP_MODE"] == "development":
        return jsonify({"success": "Provided JSON looks good"})

    payment_execute_request = payments.PaymentExecuteRequest(req["paymentID"])
    payment_execute_request.request_body({
        "payerID": req["payerID"]
    })

    try:
        payment_execute_response = pp_client.execute(payment_execute_request)
        result = payment_execute_response.result
    except IOError as ioe:
        if isinstance(ioe, braintreehttp.HttpError):
            # Something went wrong server-side
            print("Server error", file=sys.stderr)
            print(ioe.status_code, file=sys.stderr)
            print(ioe.headers["PayPal-Debug-Id"], file=sys.stderr)
        else:
            # Something went wrong client side
            traceback.print_exc()
        raise InternalServerError(jsonify({"error": "Server error"}))

    return jsonify({
        "result": result["state"]
    })


@app.route(app.config["APP_WEB_ROOT"] + '/paypal/cancel')
def paypal_cancel():
    return jsonify({"error": "This is a stub"})

@app.route(app.config["APP_WEB_ROOT"] + '/paypal/return')
def paypal_return():
    return jsonify({"error": "This is a stub"})