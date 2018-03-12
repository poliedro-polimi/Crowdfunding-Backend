from flask_sqlalchemy import SQLAlchemy

from .. import app
from poliedro_donate.database.models import *

db = SQLAlchemy(app)
