import os
import pytest

from poliedro_donate.cli import *


@pytest.fixture(scope="module", autouse=True)
def setup_app_env():
    os.environ["FLASK_APP"] = "poliedro_donate"
    yield


def test_initdb():
    with pytest.raises(SystemExit) as exc:
        initdb()
    assert exc.value.args[0] == 0


def test_cleardb():
    with pytest.raises(SystemExit) as exc:
        cleardb()
    assert exc.value.args[0] == 0
