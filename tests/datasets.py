import braintreehttp.http_response

JSON_SG0_GOOD = {
    "donation": 10,
    "stretch_goal": 0,
    "items": 0,
    "notes": "Solo donazione, PoliEdro i migliori <3",
}

JSON_SG1_GOOD = {
    "donation": 10,
    "stretch_goal": 1,
    "items": 2,
    "notes": "",
    "reference": {
        "firstname": "Davide",
        "lastname": "Depau",
        "email": "email@domain.com",
        "phone": "+393200000000",
        "location": "bovisa"
    }
}

JSON_SG2_GOOD = {
    "donation": 17,
    "stretch_goal": 2,
    "items": 3,
    "notes": "",
    "reference": {
        "firstname": "Davide",
        "lastname": "Depau",
        "email": "email@domain.com",
        "phone": "+393200000000",
        "location": "leonardo"
    }
}

JSON_SG3_GOOD = {
    "donation": 35,
    "stretch_goal": 3,
    "items": 3,
    "shirts": [
        {"size": "XS", "type": "tank-top"},
        {"size": "L", "type": "t-shirt"},
        {"size": "XXL", "type": "t-shirt"}
    ],
    "notes": "",
    "reference": {
        "firstname": "Davide",
        "lastname": "Depau",
        "email": "email@domain.com",
        "phone": "+393200000000",
        "location": "leonardo"
    }
}

JSON_NOTCOVERED = {
    "donation": 1,
    "stretch_goal": 2,
    "items": 2,
    "notes": "",
    "reference": {
        "firstname": "Davide",
        "lastname": "Depau",
        "email": "email@domain.com",
        "phone": "+393200000000",
        "location": "bovisa"
    }
}

JSON_INVALID_STRETCH_GOAL = {
    "donation": 10,
    "stretch_goal": -7,
    "items": 2,
    "notes": "",
    "reference": {
        "firstname": "Davide",
        "lastname": "Depau",
        "email": "email@domain.com",
        "phone": "+393200000000",
        "location": "bovisa"
    }
}

JSON_SG3_SHIRTS_ITEMS_MISMATCH = {
    "donation": 100,
    "stretch_goal": 3,
    "items": 5,
    "shirts": [
        {"size": "XS", "type": "tank-top"},
        {"size": "L", "type": "t-shirt"},
        {"size": "XXL", "type": "t-shirt"}
    ],
    "notes": "",
    "reference": {
        "firstname": "Davide",
        "lastname": "Depau",
        "email": "email@domain.com",
        "phone": "+393200000000",
        "location": "leonardo"
    }
}

JSON_SG3_SHIRTS_MISSING = {
    "donation": 500,
    "stretch_goal": 3,
    "items": 5,
    "notes": "",
    "reference": {
        "firstname": "Davide",
        "lastname": "Depau",
        "email": "email@domain.com",
        "phone": "+393200000000",
        "location": "leonardo"
    }
}

JSON_SGgt0_REFERENCE_MISSING = {
    "donation": 100,
    "stretch_goal": 1,
    "items": 5,
    "notes": "",
}

JSON_DONATION_NULL = {
    "donation": None,
    "stretch_goal": 0,
    "items": 0,
    "notes": "Solo donazione, PoliEdro i migliori <3"
}

JSON_STRETCH_GOAL_NULL = {
    "donation": 10,
    "stretch_goal": None,
    "items": 0,
    "notes": "Solo donazione, PoliEdro i migliori <3"
}

JSON_REFERENCE_NULL = {
    "donation": 10,
    "stretch_goal": 0,
    "items": 0,
    "notes": "Solo donazione, PoliEdro i migliori <3",
    "reference": None
}

JSON_STRETCH_GOAL_MISSING = {
    "donation": 10,
    "items": 0,
    "notes": "Solo donazione, PoliEdro i migliori <3",
    "reference": None
}

JSON_INVALID_LANG = {
    "donation": 35,
    "stretch_goal": 3,
    "items": 3,
    "shirts": [
        {"size": "XS", "type": "tank-top"},
        {"size": "L", "type": "t-shirt"},
        {"size": "XXL", "type": "t-shirt"}
    ],
    "notes": "",
    "reference": {
        "firstname": "Davide",
        "lastname": "Depau",
        "email": "email@domain.com",
        "phone": "+393200000000",
        "location": "leonardo"
    },
    "lang": "sardu"
}

JSON_VALID_LANG = {
    "donation": 35,
    "stretch_goal": 3,
    "items": 3,
    "shirts": [
        {"size": "XS", "type": "tank-top"},
        {"size": "L", "type": "t-shirt"},
        {"size": "XXL", "type": "t-shirt"}
    ],
    "notes": "",
    "reference": {
        "firstname": "Davide",
        "lastname": "Depau",
        "email": "email@domain.com",
        "phone": "+393200000000",
        "location": "leonardo"
    },
    "lang": "it"
}

REFERENCE_GOOD = {
    "firstname": "Davide",
    "lastname": "Depau",
    "email": "email@domain.com",
    "phone": "+393200000000",
    "location": "bovisa"
}

REFERENCE_WRONG_LOCATION = {
    "firstname": "Davide",
    "lastname": "Depau",
    "email": "email@domain.com",
    "phone": "+393200000000",
    "location": "bovisasca"
}

REFERENCE_WRONG_EMAIL = {
    "firstname": "Davide",
    "lastname": "Depau",
    "email": "culo",
    "phone": "+393200000000",
    "location": "leonardo"
}

REFERENCE_NAME_EMPTY = {
    "firstname": "",
    "lastname": "Depau",
    "email": "email@domain.com",
    "phone": "+393200000000",
    "location": "leonardo"
}

SHIRTS_WRONG_SIZE = [
    {"size": "XXS", "type": "tank-top"},
    {"size": "Z", "type": "t-shirt"},
    {"size": "XXX", "type": "t-shirt"}
]

SHIRTS_WRONG_TYPE = [
    {"size": "XS", "type": "tank-top"},
    {"size": "L", "type": "jockstrap"},
    {"size": "XXL", "type": "t-shirt"}
]

SAMPLE_PAYMENT_ID = "PAY-0J356327TH335450NK56Y2PQ"
SAMPLE_PAYER_ID = "3VWBNYXTUCXWY"

JSON_EXECUTE_PAYMENT_GOOD = {
    "paymentID": SAMPLE_PAYMENT_ID,
    "payerID": SAMPLE_PAYER_ID
}

JSON_EXECUTE_PAYMENT_BAD = {
    "paymentID": SAMPLE_PAYMENT_ID,
    "involtini_primavera": None
}

SAMPLE_PAYMENT_OBJ = {
    "payer": {
        "payment_method": "paypal"
    },
    "intent": "sale",
    "transactions": [{
        "amount": {
            "total": "10.0",
            "currency": "EUR"
        },
        "description": "Sample payment"
    }],
    "redirect_urls": {
        "cancel_url": "https://example.com/cancel",
        "return_url": "https://example.com/return"
    },
}

SAMPLE_PAYPAL_EMAIL = "info-buy@poliedro-polimi.it"

SAMPLE_PAYMENT_RESULT_DICT = {
    "id": "PAY-7S8766975F679581RLLAZQQA",
    "intent": "sale",
    "state": "approved",
    "cart": "0U078830GC215480U",
    "payer": {
        "payment_method": "paypal",
        "status": "VERIFIED",
        "payer_info": {
            "email": "info-buy@poliedro-polimi.it",
            "first_name": "PoliEdro",
            "last_name": "EsciISoldi",
            "payer_id": "QT8FQQDSJZKLN",
            "shipping_address": {
                "recipient_name": "PoliEdro EsciISoldi",
                "line1": "Via Unit? d'Italia, 5783296",
                "city": "Napoli",
                "state": "Napoli",
                "postal_code": "80127",
                "country_code": "IT"
            },
            "country_code": "IT"
        }
    },
    "transactions": [
        {
            "amount": {
                "total": "90.00",
                "currency": "EUR",
                "details": {}
            },
            "payee": {
                "merchant_id": "R2EFMMT372XLL",
                "email": "info-facilitator@poliedro-polimi.it"
            },
            "description": "Donation to PoliEdro - With gadget reservation: 9x PoliMi Pride Full Kit - sackpack, pins, stickers, t-shirt/tank top (id: #D19T19)",
            "item_list": {
                "shipping_address": {
                    "recipient_name": "PoliEdro EsciISoldi",
                    "line1": "Via Unit? d'Italia, 5783296",
                    "city": "Napoli",
                    "state": "Napoli",
                    "postal_code": "80127",
                    "country_code": "IT"
                }
            },
            "related_resources": [
                {
                    "sale": {
                        "id": "97H56559EV9382605",
                        "state": "completed",
                        "amount": {
                            "total": "90.00",
                            "currency": "EUR",
                            "details": {
                                "subtotal": "90.00"
                            }
                        },
                        "payment_mode": "INSTANT_TRANSFER",
                        "protection_eligibility": "ELIGIBLE",
                        "protection_eligibility_type": "ITEM_NOT_RECEIVED_ELIGIBLE,UNAUTHORIZED_PAYMENT_ELIGIBLE",
                        "transaction_fee": {
                            "value": "3.41",
                            "currency": "EUR"
                        },
                        "parent_payment": "PAY-7S8766975F679581RLLAZQQA",
                        "create_time": "2018-04-02T02:42:02Z",
                        "update_time": "2018-04-02T02:42:02Z",
                        "links": [
                            {
                                "href": "https://api.sandbox.paypal.com/v1/payments/sale/97H56559EV9382605",
                                "rel": "self",
                                "method": "GET"
                            },
                            {
                                "href": "https://api.sandbox.paypal.com/v1/payments/sale/97H56559EV9382605/refund",
                                "rel": "refund",
                                "method": "POST"
                            },
                            {
                                "href": "https://api.sandbox.paypal.com/v1/payments/payment/PAY-7S8766975F679581RLLAZQQA",
                                "rel": "parent_payment",
                                "method": "GET"
                            }
                        ]
                    }
                }
            ]
        }
    ],
    "create_time": "2018-04-02T02:42:03Z",
    "links": [
        {
            "href": "https://api.sandbox.paypal.com/v1/payments/payment/PAY-7S8766975F679581RLLAZQQA",
            "rel": "self",
            "method": "GET"
        }
    ]
}

SAMPLE_PAYMENT_RESULT_OBJ = braintreehttp.http_response.construct_object('Result', SAMPLE_PAYMENT_RESULT_DICT)


def _random_string():
    import uuid
    return str(uuid.uuid4()).split("-")[-1]


def gen_donation_jsons(n=50):
    import random
    for i in range(n):
        sg = random.randint(0, 3)
        d = globals()["JSON_SG{}_GOOD".format(sg)].copy()

        for key in d:
            if isinstance(d[key], str):
                d[key] = _random_string()

        # Generate some duplicate references
        if "reference" in d:
            d["reference"] = REFERENCE_GOOD.copy()
            if random.random() < 0.5:
                d["reference"]["firstname"] = _random_string()

        yield d, _random_string(), {"key": _random_string()}
