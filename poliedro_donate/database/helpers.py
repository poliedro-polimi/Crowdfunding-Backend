__all__ = ('commit_on_success', 'json2db_shirt', 'db2json_shirt')

from functools import wraps

from .database import db
from .models import Shirt
from ..validator import SHIRT_SIZES, SHIRT_TYPES


# https://gist.github.com/yashh/14d12595f3dfa307a354
def commit_on_success(func):
    def _commit_on_success(*args, **kw):
        try:
            res = func(*args, **kw)
        except Exception:
            if db.session.dirty:
                db.session.rollback()
            raise
        else:
            if db.session.dirty:
                try:
                    db.session.commit()
                except Exception:
                    db.session.rollback()
                    raise
        return res

    return wraps(func)(_commit_on_success)


def json2db_shirt(s: dict) -> dict:
    return {
        "size": SHIRT_SIZES.index(s["size"].upper()),
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
