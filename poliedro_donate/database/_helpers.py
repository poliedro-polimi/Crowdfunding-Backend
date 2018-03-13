from .models import Shirt
from ..validator import SHIRT_SIZES, SHIRT_TYPES


def json2db_shirt(s: dict) -> dict:
    return {
        "size": SHIRT_SIZES.index(s["size"]),
        "type": SHIRT_TYPES.index(s["type"])
    }


def db2json_shirt(s: Shirt) -> dict:
    return {
        "size": SHIRT_SIZES[s.size],
        "type": SHIRT_TYPES[s.type]
    }


def deconstruct_object(obj) -> dict:
    dest = {}
    for key in (i for i in dir(obj) if not i.startswith("_")):
        dest[key] = getattr(obj, key)

    return dest
