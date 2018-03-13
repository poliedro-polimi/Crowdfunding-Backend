from socket import gethostname

from . import app
from .database import db

db.create_all()

# Avoid running app in PythonAnywhere's console
# https://help.pythonanywhere.com/pages/Flask/
if 'liveconsole' not in gethostname():
    app.run()
