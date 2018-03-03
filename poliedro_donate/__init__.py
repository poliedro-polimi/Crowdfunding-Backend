from flask import Flask, abort, g, request, session, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel

from poliedro_donate.config import DefaultConfig

app = Flask(__name__)
app.config.from_object(DefaultConfig)
app.config.from_envvar('POLIEDRO_DONATE_CONFIG')

db = SQLAlchemy(app)
# babel = Babel(app)

#
# @babel.localeselector
# def get_locale():
#     return g.get('lang_code', app.config['BABEL_DEFAULT_LOCALE'])
#
#
# @babel.timezoneselector
# def get_timezone():
#     user = g.get('user', None)
#     if user is not None:
#         return user.timezone
#
# @app.url_defaults
# def set_language_code(endpoint, values):
#     if 'lang_code' in values or not g.get('lang_code', None):
#         return
#     if app.url_map.is_endpoint_expecting(endpoint, 'lang_code'):
#         values['lang_code'] = g.lang_code
#
# @app.url_value_preprocessor
# def get_lang_code(endpoint, values):
#     if values is not None:
#         g.lang_code = values.pop('lang_code', None)
#
#
# @app.before_request
# def ensure_lang_support():
#     lang_code = g.get('lang_code', None)
#     if lang_code and lang_code not in app.config['SUPPORTED_LANGUAGES'].keys():
#         return abort(404)

# main = Blueprint('main', __name__, template_folder='templates')

# app.register_blueprint(main, url_prefix='/')
# app.register_blueprint(main, url_prefix='/<lang_code>/')

#
# @app.before_request
# def update_language_code():
#     if "lang" in request.args:
#         session.lang_code = request.args["lang"]
#         session.permanent = True
#         g.lang_code = session.lang_code


from .views import *
