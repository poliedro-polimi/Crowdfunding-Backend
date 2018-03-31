def get_paypal_email(res):
    try:
        return res["payer"]["payer_info"]["email"]
    except KeyError:
        return None