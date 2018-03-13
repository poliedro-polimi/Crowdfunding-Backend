import pytest

from poliedro_donate.validator import *
from .datasets import *


def test_sg0_good():
    validate_donation_request(JSON_SG0_GOOD)


def test_sg1_good():
    validate_donation_request(JSON_SG1_GOOD)


def test_sg2_good():
    validate_donation_request(JSON_SG2_GOOD)


def test_sg3_good():
    validate_donation_request(JSON_SG3_GOOD)


def test_costs_not_covered():
    with pytest.raises(ValueError) as exc:
        validate_donation_request(JSON_NOTCOVERED)
    assert "Provided donation does not cover the purchase of the selected gadgets" in str(exc)


def test_invalid_stretch_goal():
    with pytest.raises(ValueError) as exc:
        validate_donation_request(JSON_INVALID_STRETCH_GOAL)
    assert "is not a valid stretch goal" in str(exc)


def test_shirts_items_mismatch():
    with pytest.raises(ValueError) as exc:
        validate_donation_request(JSON_SG3_SHIRTS_ITEMS_MISMATCH)
    assert "Shirts quantity and item quantity don't match" in str(exc)


def test_invalid_lang():
    with pytest.raises(ValueError) as exc:
        validate_donation_request(JSON_INVALID_LANG)
    assert "Unsupported lang" in str(exc)


def test_valid_lang():
    validate_donation_request(JSON_VALID_LANG)


def test_shirts_missing():
    with pytest.raises(KeyError) as exc:
        validate_donation_request(JSON_SG3_SHIRTS_MISSING)
    assert "shirts" in str(exc)


def test_reference_missing():
    with pytest.raises(KeyError) as exc:
        validate_donation_request(JSON_SGgt0_REFERENCE_MISSING)
    assert "reference" in str(exc)


def test_reference_null():
    with pytest.raises(TypeError):
        validate_donation_request(JSON_REFERENCE_NULL)


def test_donation_null():
    with pytest.raises(TypeError):
        validate_donation_request(JSON_DONATION_NULL)


def test_stretch_goal_null():
    with pytest.raises(ValueError) as exc:
        validate_donation_request(JSON_STRETCH_GOAL_NULL)
    assert "is not a valid stretch goal" in str(exc)


def test_stretch_goal_missing():
    with pytest.raises(KeyError) as exc:
        validate_donation_request(JSON_STRETCH_GOAL_MISSING)
    assert "stretch_goal" in str(exc)


def test_reference_wrong_email():
    with pytest.raises(ValueError) as exc:
        validate_reference(REFERENCE_WRONG_EMAIL)
    assert "Email address is invalid" in str(exc)


def test_reference_wrong_location():
    with pytest.raises(ValueError) as exc:
        validate_reference(REFERENCE_WRONG_LOCATION)
    assert "Invalid location" in str(exc)


def test_reference_name_empty():
    with pytest.raises(ValueError) as exc:
        validate_reference(REFERENCE_NAME_EMPTY)
    assert "Empty string" in str(exc)


def test_shirts_wrong_size():
    with pytest.raises(ValueError) as exc:
        validate_shirts(SHIRTS_WRONG_SIZE)
    assert "is not a valid shirt size" in str(exc)


def test_shirts_wrong_type():
    with pytest.raises(ValueError) as exc:
        validate_shirts(SHIRTS_WRONG_TYPE)
    assert "is not a valid shirt type" in str(exc)
