import os
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

from .cli import *
from .errors import *
from .blueprints.paypal import paypal_bp

app.register_blueprint(paypal_bp, url_prefix='/paypal')
