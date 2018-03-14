import os
from flask import Flask

from poliedro_donate.config import DefaultConfig

app = Flask(__name__)
app.config.from_object(DefaultConfig)

if 'POLIEDRO_DONATE_CONFIG' in os.environ:
    app.config.from_envvar('POLIEDRO_DONATE_CONFIG')

if app.config.get("APP_ENABLE_CORS", False):
    from flask_cors import CORS

    CORS(app)

from .cli import *
from .errors import *
from .views import *
