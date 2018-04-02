import pytest

from poliedro_donate.utils import get_paypal_email
from .datasets import *

from poliedro_donate import app as application
from poliedro_donate.mail import send_confirmation_email

from poliedro_donate.database import db, register_donation, register_transaction


@pytest.fixture
def app():
    application.config["APP_MODE"] = "development"
    return application


@pytest.fixture(scope='module')
def donation():
    db.session.commit()
    db.reflect()
    db.drop_all()
    db.create_all()
    db.reflect()
    db.session.commit()

    # Create sample donation
    d = register_donation(JSON_SG3_GOOD, SAMPLE_PAYMENT_ID, SAMPLE_PAYMENT_OBJ)
    register_transaction(SAMPLE_PAYMENT_ID, SAMPLE_PAYER_ID, SAMPLE_PAYMENT_RESULT_DICT,
                         SAMPLE_PAYMENT_RESULT_OBJ.state)

    db.session.commit()

    yield d

    db.session.commit()
    db.reflect()
    db.drop_all()
    db.session.commit()


def test_get_paypal_email():
    assert get_paypal_email(SAMPLE_PAYMENT_RESULT_DICT) == SAMPLE_PAYPAL_EMAIL


def test_email_confirmation_en(app, donation):
    with app.test_request_context('/paypal/execute', method='POST'):
        send_confirmation_email("bogus@example.com", donation, "en", dryrun=True)


def test_email_confirmation_it(app, donation):
    with app.test_request_context('/paypal/execute', method='POST'):
        send_confirmation_email("bogus@example.com", donation, "it", dryrun=True)
