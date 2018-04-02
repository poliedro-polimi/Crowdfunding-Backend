import base64
import json, pytest, sys
from flask import url_for
from werkzeug.datastructures import Headers

from poliedro_donate.database import register_donation, register_transaction, db
from poliedro_donate.database.models import AdminUser

from .datasets import *

from poliedro_donate import app as application

if sys.version_info.major == 2:
    # noinspection PyShadowingBuiltins
    bytes = str
    # noinspection PyUnresolvedReferences,PyShadowingBuiltins
    str = unicode


def _auth_header(user, pwd):
    d = Headers()
    d.add("Authorization", "Basic {}".format(base64.b64encode("{}:{}".format(user, pwd).encode()).decode()))
    print(d)
    return d


@pytest.fixture
def app():
    application.config["APP_MODE"] = "development"
    application.config["PAYPAL_CLIENT_ID"] = "invalid"
    application.config["PAYPAL_CLIENT_SECRET"] = "invalid"
    application.debug = True  # Required to avoid SSL redirects in tests
    return application


@pytest.fixture(autouse=True)
def setup_cleanup_tests():
    db.session.commit()
    db.reflect()
    db.drop_all()
    db.create_all()
    db.reflect()
    db.session.commit()
    u = AdminUser('test', 'test')
    db.session.add(u)
    db.session.commit()
    yield


def test_paypal_create_payment_good(client):
    r = client.post(url_for('paypal.create_payment') + "?validate_only=1",
                    data=json.dumps(JSON_SG0_GOOD),
                    content_type="application/json")

    if isinstance(r.data, bytes):
        j = json.loads(r.data.decode())
    else:
        j = json.loads(r.data)

    assert r.status_code == 200
    assert j == {"success": "Provided JSON looks good"}


def test_paypal_create_payment_bad(client):
    r = client.post(url_for('paypal.create_payment') + "?validate_only=1",
                    data=json.dumps(JSON_STRETCH_GOAL_MISSING),
                    content_type="application/json")

    if isinstance(r.data, bytes):
        j = json.loads(r.data.decode())
    else:
        j = json.loads(r.data)

    assert r.status_code == 400
    assert j["error"]["type"] == "_VALIDATION_ERROR"


def test_paypal_create_payment_paypal_error(client):
    # validate_only is not specified and auth credentials are invalid
    r = client.post(url_for('paypal.create_payment'),
                    data=json.dumps(JSON_SG0_GOOD),
                    content_type="application/json")

    if isinstance(r.data, bytes):
        j = json.loads(r.data.decode())
    else:
        j = json.loads(r.data)

    assert r.status_code == 502
    assert j["error"]["type"] == "_PAYPAL_ERROR"


def test_paypal_execute_payment_good(client):
    r = client.post(url_for('paypal.execute_payment') + "?validate_only=1",
                    data=json.dumps(JSON_EXECUTE_PAYMENT_GOOD),
                    content_type="application/json")

    if isinstance(r.data, bytes):
        j = json.loads(r.data.decode())
    else:
        j = json.loads(r.data)

    assert r.status_code == 200
    assert j == {"success": "Provided JSON looks good"}


def test_paypal_execute_payment_bad(client):
    r = client.post(url_for('paypal.execute_payment') + "?validate_only=1",
                    data=json.dumps(JSON_EXECUTE_PAYMENT_BAD),
                    content_type="application/json")

    if isinstance(r.data, bytes):
        j = json.loads(r.data.decode())
    else:
        j = json.loads(r.data)

    assert r.status_code == 400
    assert j["error"]["type"] == "_VALIDATION_ERROR"


def test_paypal_execute_payment_paypal_error(client):
    d = register_donation(JSON_SG0_GOOD, SAMPLE_PAYMENT_ID, SAMPLE_PAYMENT_OBJ)
    register_transaction(SAMPLE_PAYMENT_ID, SAMPLE_PAYER_ID, SAMPLE_PAYMENT_RESULT_DICT,
                         SAMPLE_PAYMENT_RESULT_OBJ.state)

    # validate_only is not specified and auth credentials are invalid
    r = client.post(url_for('paypal.execute_payment'),
                    data=json.dumps(JSON_EXECUTE_PAYMENT_GOOD),
                    content_type="application/json")

    if isinstance(r.data, bytes):
        j = json.loads(r.data.decode())
    else:
        j = json.loads(r.data)

    assert r.status_code == 502
    assert j["error"]["type"] == "_PAYPAL_ERROR"


def test_donations_list(client):
    r = client.get(url_for('donations.list_all'), follow_redirects=True, headers=_auth_header('test', 'test'))
    assert r.status_code == 200


def test_by_location_bovisa(client):
    r = client.get(url_for('donations.by_location', location="bovisa"), follow_redirects=True,
                   headers=_auth_header('test', 'test'))
    assert r.status_code == 200


def test_by_location_leonardo(client):
    r = client.get(url_for('donations.by_location', location="leonardo"), follow_redirects=True,
                   headers=_auth_header('test', 'test'))
    assert r.status_code == 200


def test_by_location_bogus(client):
    r = client.get(url_for('donations.by_location', location="bogus"), follow_redirects=True,
                   headers=_auth_header('test', 'test'))
    assert r.status_code == 404


def test_print_labels_bovisa(client):
    r = client.get(url_for('donations.print_labels', location="bovisa"), follow_redirects=True,
                   headers=_auth_header('test', 'test'))
    assert r.status_code == 200


def test_print_labels_leonardo(client):
    r = client.get(url_for('donations.print_labels', location="leonardo"), follow_redirects=True,
                   headers=_auth_header('test', 'test'))
    assert r.status_code == 200


def test_print_labels_bogus(client):
    r = client.get(url_for('donations.print_labels', location="bogus"), follow_redirects=True,
                   headers=_auth_header('test', 'test'))
    assert r.status_code == 404


def test_donation_notexist(client):
    r = client.get(url_for('donations.donation', d_id=999, t_id=999), follow_redirects=True,
                   headers=_auth_header('test', 'test'))
    assert r.status_code == 404


def test_reference_notexist(client):
    r = client.get(url_for('donations.reference', r_id=999), follow_redirects=True,
                   headers=_auth_header('test', 'test'))
    assert r.status_code == 404


def test_to_order(client):
    r = client.get(url_for('donations.to_order'), follow_redirects=True, headers=_auth_header('test', 'test'))
    assert r.status_code == 200


def test_auth_wrong(client):
    r = client.get(url_for('donations.list_all'), follow_redirects=True, headers=_auth_header('penis', 'dick'))
    assert r.status_code == 401


def test_no_auth(client):
    r = client.get(url_for('donations.list_all'), follow_redirects=True, headers=_auth_header('penis', 'dick'))
    assert r.status_code == 401


def test_ssl_redirect(app, client):
    old_debug = app.debug
    app.debug = False
    try:
        r = client.get(url_for('donations.list_all'), headers=_auth_header('test', 'test'))
        assert r.status_code == 301
        assert r.headers.get('Location').startswith("https://")
    finally:
        app.debug = old_debug

