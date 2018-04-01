__all__ = ('STRETCH_GOAL_PRICES', 'SHIRT_TYPES', 'SHIRT_SIZES', 'LOCATIONS', 'email_re', 'describe_error',
           'validate_donation_request', 'validate_lang', 'validate_donation', 'validate_reference', 'validate_location',
           'validate_items', 'validate_stretch_goal', 'validate_shirts', 'validate_shirt', 'validate_shirt_size',
           'validate_shirt_type', 'validate_email', 'validate_string', 'validate_execute_request')

import re, sys
from functools import wraps

from poliedro_donate import strings

STRETCH_GOAL_PRICES = {
    0: 0.0,
    1: 2.0,
    2: 5.0,
    3: 10.0
}

SHIRT_TYPES = ("tank-top", "t-shirt")
SHIRT_SIZES = ("XS", "S", "M", "L", "XL", "XXL")

LOCATIONS = ("leonardo", "bovisa")

# From http://emailregex.com/
email_re = re.compile(
    r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])")


def describe_error(name, format_args=False):
    def decorator(f):
        @wraps(f)
        def wrapper(*a, **kw):
            try:
                return f(*a, **kw)
            except Exception as e:
                if format_args:
                    fname = name.format(*a, **kw)
                else:
                    fname = name

                edesc = getattr(e, "edesc", None)
                if not edesc:
                    e.edesc = fname
                else:
                    e.edesc = fname + "." + edesc

                raise e

        return wrapper

    return decorator


@describe_error("create()")
def validate_donation_request(req):
    if not isinstance(req, dict):
        raise ValueError("Invalid request")
    validate_stretch_goal(req["stretch_goal"])
    validate_items(req["items"])
    validate_donation(req["donation"], req["stretch_goal"], req["items"])
    validate_string(req["notes"], key="notes")
    if "lang" in req:
        validate_lang(req["lang"])
    if req["stretch_goal"] > 0 or "reference" in req:
        validate_reference(req["reference"])
    if req["stretch_goal"] >= 3:
        if len(req["shirts"]) != req["items"]:
            raise ValueError("Shirts quantity and item quantity don't match")
        validate_shirts(req["shirts"])

    return True


@describe_error("lang")
def validate_lang(lang):
    if lang not in strings.LANGS:
        raise ValueError("Unsupported lang: {}".format(lang))


@describe_error("donation")
def validate_donation(donation, stretch_goal, items):
    float(donation)
    min_price = STRETCH_GOAL_PRICES[stretch_goal] * items
    if donation < min_price:
        raise ValueError(
            "Provided donation does not cover the purchase of the selected gadgets. Minimum: {} EUR for {} items of "
            "type {}. Provided: {} EUR".format(
                min_price, items, stretch_goal, donation))


@describe_error("reference")
def validate_reference(ref):
    dict(ref)
    validate_string(ref["firstname"], True, key="firstname")
    validate_string(ref["lastname"], True, key="firstname")
    validate_email(ref["email"])
    validate_string(ref["phone"], key="phone")
    validate_location(ref["location"])


@describe_error("location")
def validate_location(loc):
    if loc not in LOCATIONS:
        raise ValueError("Invalid location: {}".format(loc))


@describe_error("items")
def validate_items(items):
    int(items)


@describe_error("stretch_goal")
def validate_stretch_goal(sg):
    if not sg in STRETCH_GOAL_PRICES:
        raise ValueError("'{}' is not a valid stretch goal".format(sg))


@describe_error("shirts")
def validate_shirts(shirts):
    list(shirts)
    for s in shirts:
        validate_shirt(s)


@describe_error("shirt")
def validate_shirt(shirt):
    dict(shirt)
    validate_shirt_size(shirt["size"])
    validate_shirt_type(shirt["type"])


@describe_error("shirt_size")
def validate_shirt_size(size):
    if size.upper() not in SHIRT_SIZES:
        raise ValueError("'{}' is not a valid shirt size".format(size))


@describe_error("shirt_type")
def validate_shirt_type(stype):
    if stype not in SHIRT_TYPES:
        raise ValueError("'{}' is not a valid shirt type".format(stype))


@describe_error("email")
def validate_email(email):
    if not email_re.match(email):
        raise ValueError("Email address is invalid")


@describe_error("str({key})", format_args=True)
def validate_string(string, not_empty=False, key=""):
    if not isinstance(string, bytes) and not isinstance(string, str):
        raise ValueError("'{}' is not a string".format(string))
    if len(string) == 0 and not_empty:
        raise ValueError("Empty string")


# noinspection PyStatementEffect
@describe_error("execute()")
def validate_execute_request(req):
    if not isinstance(req, dict):
        raise ValueError("Invalid request")
    req["payerID"]
    req["paymentID"]
    if "lang" in req:
        validate_lang(req["lang"])
