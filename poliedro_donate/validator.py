import re, sys

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

if sys.version_info.major == 2:
    # noinspection PyShadowingBuiltins
    bytes = str
    # noinspection PyShadowingBuiltins
    str = unicode

# From http://emailregex.com/
email_re = re.compile(
    r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])")


def validate_donation_request(req):
    validate_stretch_goal(req["stretch_goal"])
    validate_items(req["items"])
    validate_donation(req["donation"], req["stretch_goal"], req["items"])
    validate_string(req["notes"])
    if "lang" in req:
        validate_lang(req["lang"])
    if req["stretch_goal"] > 0 or "reference" in req:
        validate_reference(req["reference"])
    if req["stretch_goal"] >= 3:
        if len(req["shirts"]) != req["items"]:
            raise ValueError("Shirts quantity and item quantity don't match")
        validate_shirts(req["shirts"])

    return True


def validate_lang(lang):
    if lang not in strings.LANGS:
        raise ValueError("Unsupported lang: {}".format(lang))


def validate_donation(donation, stretch_goal, items):
    float(donation)
    min_price = STRETCH_GOAL_PRICES[stretch_goal] * items
    if donation < min_price:
        raise ValueError(
            "Provided donation does not cover the purchase of the selected gadgets. Minimum: {} EUR for {} items of "
            "type {}. Provided: {} EUR".format(
                min_price, items, stretch_goal, donation))


def validate_reference(ref):
    dict(ref)
    validate_string(ref["firstname"], True)
    validate_string(ref["lastname"], True)
    validate_email(ref["email"])
    validate_string(ref["phone"])
    validate_location(ref["location"])


def validate_location(loc):
    if loc not in LOCATIONS:
        raise ValueError("Invalid location: {}".format(loc))


def validate_items(items):
    int(items)


def validate_stretch_goal(sg):
    if not sg in STRETCH_GOAL_PRICES:
        raise ValueError("'{}' is not a valid stretch goal".format(sg))


def validate_shirts(shirts):
    list(shirts)
    for s in shirts:
        validate_shirt(s)


def validate_shirt(shirt):
    dict(shirt)
    validate_shirt_size(shirt["size"])
    validate_shirt_type(shirt["type"])


def validate_shirt_size(size):
    if size.upper() not in SHIRT_SIZES:
        raise ValueError("'{}' is not a valid shirt size".format(size))


def validate_shirt_type(stype):
    if stype not in SHIRT_TYPES:
        raise ValueError("'{}' is not a valid shirt type".format(stype))


def validate_email(email):
    if not email_re.match(email):
        raise ValueError("Email address is invalid")


def validate_string(string, not_empty=False):
    if not isinstance(string, bytes) and not isinstance(string, str):
        raise ValueError("'{}' is not a string".format(string))
    if len(string) == 0 and not_empty:
        raise ValueError("Empty string")


# noinspection PyStatementEffect
def validate_execute_request(req):
    req["payerID"]
    req["paymentID"]
    validate_lang(req["lang"])
