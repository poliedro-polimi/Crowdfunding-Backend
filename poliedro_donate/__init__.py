__all__ = (
    'app', 'babel', 'blueprints', 'database', 'auth', 'cli', 'config',
    'errors', 'mail', 'paypal', 'strings', 'utils', 'validator'
)

import os, json
from flask import Flask, g
from flask_babel import Babel

from poliedro_donate.config import DefaultConfig

app = Flask(__name__)
app.config.from_object(DefaultConfig)

if 'POLIEDRO_DONATE_CONFIG' in os.environ:
    app.config.from_envvar('POLIEDRO_DONATE_CONFIG')

if app.config.get("APP_ENABLE_CORS", False):
    from flask_cors import CORS

    CORS(app)

babel = Babel(app)


@babel.localeselector
def get_locale():
    return getattr(g, "lang", "en")


app.jinja_env.globals['json'] = json
app.jinja_env.globals['len'] = len

from .cli import *
from .errors import *
from .blueprints.paypal import paypal_bp
from .blueprints.donations import donations_bp

app.register_blueprint(paypal_bp, url_prefix='/paypal')
app.register_blueprint(donations_bp, url_prefix='/donations')
