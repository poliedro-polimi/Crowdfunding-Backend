from __future__ import print_function

import json
import sys, traceback
from flask import request, jsonify, url_for

from . import app, strings, database
from .utils import validate_donation_request, validate_execute_request
from .paypal import pp_client

import paypalrestsdk.v1.payments as payments


@app.route(app.config["APP_WEB_ROOT"] + '/paypal/create', methods=('POST',))
def paypal_create_payment():
    req = request.get_json()

    try:
        validate_donation_request(req)
    except Exception:
        traceback.print_exc(file=sys.stderr)
        raise

    if "lang" in req:
        lang = req["lang"]
    else:
        lang = "en"

    if int(request.args.get("validate_only", 0)) and app.config["APP_MODE"] == "development":
        return jsonify({"success": "Provided JSON looks good"})

    body = {
        "payer": {
            "payment_method": "paypal"
        },
        "intent": "sale",
        "transactions": [{
            "amount": {
                "total": str(req["donation"]),
                "currency": "EUR"
            },
            "description": strings.PP_ITEM_NAME[lang] + " - " + strings.PP_ITEM_DESC(lang, req["stretch_goal"],
                                                                                     req["items"])
        }],
        "redirect_urls": {
            "cancel_url": url_for("paypal_cancel"),
            "return_url": url_for("paypal_return")
        },
    }

    payment_create_request = payments.PaymentCreateRequest()
    payment_create_request.request_body(body)

    try:
        payment_create_response = pp_client.execute(payment_create_request)
        payment = payment_create_response.result
    except IOError as ioe:
        ioe.body = body
        raise

    # Store request into database
    database.register_donation(req, payment.id, json.dumps(body))

    return jsonify({"paymentID": payment.id})


@app.route(app.config["APP_WEB_ROOT"] + '/paypal/execute', methods=('POST',))
def paypal_execute():
    req = request.json

    try:
        validate_execute_request(req)
    except Exception:
        traceback.print_exc(file=sys.stderr)
        raise

    if int(request.args.get("validate_only", 0)) and app.config["APP_MODE"] == "development":
        return jsonify({"success": "Provided JSON looks good"})

    body = {
        "payer_id": req["payerID"]
    }

    payment_execute_request = payments.PaymentExecuteRequest(req["paymentID"])
    payment_execute_request.request_body(body)

    try:
        payment_execute_response = pp_client.execute(payment_execute_request)
        result = payment_execute_response.result
    except IOError as ioe:
        ioe.body = body
        raise

    # Store payment execution into database
    database.register_transaction(req["paymentID"], req["payerID"], result, result.state)

    return jsonify({
        "result": result.state
    })


@app.route(app.config["APP_WEB_ROOT"] + '/paypal/cancel')
def paypal_cancel():
    return jsonify({"error": "This is a stub"})


@app.route(app.config["APP_WEB_ROOT"] + '/paypal/return')
def paypal_return():
    return jsonify({"error": "This is a stub"})
