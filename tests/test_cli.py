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


def test_add_del_user():
    db.drop_all()
    db.session.commit()
    db.create_all()
    db.session.commit()
    with pytest.raises(SystemExit) as exc:
        adduser(['test', 'Test', 'User', 'password'])
    assert exc.value.args[0] == 0

    u = AdminUser.query.filter_by(username='test')
    assert u.count() == 1
    assert u[0].check_password('password')

    with pytest.raises(SystemExit) as exc:
        deluser(['test'])
    assert exc.value.args[0] == 0

    u = AdminUser.query.filter_by(username='test')
    assert u.count() == 0
    db.drop_all()
    db.session.commit()


def test_user_chpasswd():
    db.drop_all()
    db.session.commit()
    db.create_all()
    db.session.commit()
    with pytest.raises(SystemExit) as exc:
        adduser(['test', 'Test', 'User', 'password'])
    assert exc.value.args[0] == 0

    with pytest.raises(SystemExit) as exc:
        passwd(['test', 'newpassword'])
    assert exc.value.args[0] == 0

    u = AdminUser.query.filter_by(username='test')
    assert u.count() == 1
    assert u[0].check_password('newpassword')

    with pytest.raises(SystemExit) as exc:
        deluser(['test'])
    assert exc.value.args[0] == 0

    u = AdminUser.query.filter_by(username='test')
    assert u.count() == 0
    db.drop_all()
    db.session.commit()