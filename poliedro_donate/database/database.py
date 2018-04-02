__all__ = ("db", "register_donation", "register_transaction", "register_reference", "add_transaction_details")

from .. import app
from flask_sqlalchemy import SQLAlchemy as SQLAlchemyBase

import json
import warnings
from typing import AnyStr, cast


class SQLAlchemy(SQLAlchemyBase):
    def apply_pool_defaults(self, app, options):
        super(SQLAlchemy, self).apply_pool_defaults(app, options)
        options["pool_pre_ping"] = True


db = SQLAlchemy(app)

from .helpers import commit_on_success, json2db_shirt, deconstruct_object
from .models import Donation, Transaction, Shirt, User


@commit_on_success
def register_donation(req: dict, payment_id: str = None, payment_obj: dict = None) -> Donation:
    if "reference" in req:
        user = register_reference(req["reference"], lang=req.get("lang", "en"))
    else:
        user = None

    t = Transaction(payment_id=payment_id if payment_id else None,
                    payment_obj=json.dumps(payment_obj) if payment_obj else None)
    donation = Donation(
        amount=req["donation"],
        stretch_goal=req["stretch_goal"],
        items=req["items"],
        notes=req["notes"] if "notes" in req else "",
        reference=user,
        transaction=t
    )
    db.session.add(t)
    db.session.add(donation)

    # Ensure donation.id (primary key) is assigned
    db.session.commit()

    if "shirts" in req:
        for s in req["shirts"]:
            dbs = Shirt(donation=donation, **(json2db_shirt(s)))
            db.session.add(dbs)

    return donation


@commit_on_success
def add_transaction_details(d: Donation, payment_id: str, payment_obj: dict):
    d.transaction.payment_id = payment_id
    d.transaction.payment_obj = json.dumps(payment_obj)


@commit_on_success
def register_transaction(payment_id: AnyStr, payer_id: AnyStr, result, state: AnyStr):
    if not isinstance(result, dict):
        result = deconstruct_object(result)

    query = Transaction.query.filter_by(payment_id=payment_id)
    t = cast(Transaction, query[0])

    t.payer_id = payer_id
    t.state = state
    t.result_obj = json.dumps(result)


def register_reference(json: dict, lang: AnyStr) -> User:
    query = User.query.filter_by(lang=lang, **json)
    count = query.count()

    if count > 1:
        warnings.warn("Duplicate users found in database (last name: '{}')".format(json["lastname"]),
                      UserWarning)

    if count >= 1:
        user = query[0]
    else:
        user = User(lang=lang, **json)
        db.session.add(user)

    return user
