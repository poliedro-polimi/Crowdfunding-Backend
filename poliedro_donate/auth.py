__all__ = ('check_auth', 'authenticate', 'requires_auth')

from functools import wraps
from flask import request, Response

from .database.models import AdminUser


# From http://flask.pocoo.org/snippets/8/

def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    query = AdminUser.query.filter_by(username=username)
    if query.count() != 1:
        return False

    u = query[0]
    return u.check_password(password)


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)

    return decorated
