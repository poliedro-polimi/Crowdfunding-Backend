import json

import pytest
from typing import cast

from poliedro_donate import app
from poliedro_donate.database import db
from poliedro_donate.database.helpers import json2db_shirt, db2json_shirt
from poliedro_donate.database.database import register_donation, register_transaction, register_reference
from poliedro_donate.database.models import *

from .datasets import *


@pytest.fixture(scope="module", autouse=True)
def create_db():
    # Ensure we're not deleting production db
    assert app.config["APP_MODE"] == "development"
    yield


@pytest.fixture(autouse=True)
def setup_cleanup_tests():
    db.reflect()
    db.drop_all()
    db.create_all()
    db.reflect()
    yield


def _check_transaction(t, payment_id, payment_obj, payer_id=None, state=None, result_obj=None):
    assert json.loads(t.payment_obj) == payment_obj
    assert t.state == state
    assert t.payment_id == payment_id
    assert t.payer_id == payer_id
    if result_obj is None:
        assert t.result_obj is None
    else:
        assert json.loads(t.result_obj) == result_obj


def _check_reference(r: User, firstname, lastname, email, phone, location, lang="en"):
    assert r.firstname == firstname
    assert r.lastname == lastname
    assert r.email == email
    assert r.phone == phone
    assert r.location == location
    assert r.lang == lang


def _check_donation(d: Donation, req: dict):
    for i in ('amount', 'stretch_goal', 'items', 'notes'):
        if i in req:
            if getattr(d, i) != req[i]:
                raise AssertionError("d.{0} == {0}".format(i))


def _check_shirts(d: Donation, shirts: list):
    assert len(d.shirts) == len(shirts)

    # Check in both directions
    for dbs in d.shirts:
        s = db2json_shirt(dbs)
        assert s in shirts
    for s in shirts:
        query = Shirt.query.filter_by(**(json2db_shirt(s)))
        assert query.count() > 0


def _check_register_donation(req, payment_id, payment_obj, sg):
    has_reference = False
    has_shirts = False

    if sg > 0:
        has_reference = True

    if sg >= 3:
        has_shirts = True

    register_donation(req, payment_id, payment_obj)

    dquery = Donation.query.filter_by(amount=req["donation"],
                                      stretch_goal=req["stretch_goal"],
                                      items=req["items"])

    assert dquery.count() == 1

    d = cast(Donation, dquery[0])

    _check_transaction(d.transaction, payment_id, payment_obj)
    if has_reference:
        _check_reference(d.reference, **req["reference"])
    if has_shirts:
        _check_shirts(d, req["shirts"])

    _check_donation(d, req)

    db.session.delete(d.transaction)
    if has_reference:
        db.session.delete(d.reference)
    db.session.delete(d)
    db.session.commit()


def _check_register_transaction(donation_req, payment_id, payment_obj, payer_id, result_obj, result_dict):
    d = register_donation(donation_req, payment_id, payment_obj)
    register_transaction(payment_id, payer_id, result_obj, result_obj.state)

    tq = Transaction.query.filter_by(payment_id=payment_id)
    assert tq.count() == 1

    t = tq[0]

    _check_donation(d, donation_req)
    _check_transaction(t, payment_id, payment_obj, payer_id, result_obj.state, result_dict)

    db.session.delete(t)
    db.session.delete(d)


def test_create_sg0_good():
    _check_register_donation(JSON_SG0_GOOD, SAMPLE_PAYMENT_ID, SAMPLE_PAYMENT_OBJ, 0)


def test_create_sg1_good():
    _check_register_donation(JSON_SG1_GOOD, SAMPLE_PAYMENT_ID, SAMPLE_PAYMENT_OBJ, 1)


def test_create_sg2_good():
    _check_register_donation(JSON_SG2_GOOD, SAMPLE_PAYMENT_ID, SAMPLE_PAYMENT_OBJ, 2)


def test_create_sg3_good():
    _check_register_donation(JSON_SG3_GOOD, SAMPLE_PAYMENT_ID, SAMPLE_PAYMENT_OBJ, 3)


def test_duplicate_reference():
    r1 = register_reference(REFERENCE_GOOD, lang="en")
    r2 = register_reference(REFERENCE_GOOD, lang="en")
    db.session.commit()

    assert r1 == r2


def test_create_many():
    json_list = []
    ref_set = set()

    for j, payment_id, payment_obj in gen_donation_jsons():
        json_list.append((j, payment_id, payment_obj))
        if "reference" in j:
            ref_set.add(frozenset(j["reference"].items()))
        register_donation(j, payment_id, payment_obj)

    db.session.commit()

    assert len(Donation.query.all()) == len(json_list)
    assert len(User.query.all()) == len(ref_set)

    for j, payment_id, payment_obj in json_list:
        tq = Transaction.query.filter_by(payment_id=payment_id)
        assert tq.count() == 1
        t = tq[0]
        d = t.donation

        _check_donation(d, j)
        _check_transaction(t, payment_id, payment_obj)

        if "shirts" in j:
            _check_shirts(d, j["shirts"])
        if "reference" in j:
            _check_reference(d.reference, **j["reference"])

    for d in Donation.query.all():
        db.session.delete(d)

    for u in User.query.all():
        db.session.delete(u)

    for t in Transaction.query.all():
        db.session.delete(t)

    db.session.commit()

    # Shirts should have been cascade-deleted
    assert len(Shirt.query.all()) == 0


def test_payment_execute():
    _check_register_transaction(JSON_SG3_GOOD, SAMPLE_PAYMENT_ID, SAMPLE_PAYMENT_OBJ, SAMPLE_PAYER_ID,
                                SAMPLE_PAYMENT_RESULT_OBJ, SAMPLE_PAYMENT_RESULT_DICT)
