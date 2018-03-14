import click
from socket import gethostname

from . import app
from .database import db, commit_on_success


def main():
    commit_on_success(db.create_all)()

    # Avoid running app in PythonAnywhere's console
    # https://help.pythonanywhere.com/pages/Flask/
    if 'liveconsole' not in gethostname():
        app.run()


@app.cli.command()
@commit_on_success
def initdb():
    """Initialize the database."""

    click.echo('Initializing database')
    db.create_all()


@app.cli.command()
@commit_on_success
def cleardb():
    """Clear the database."""
    click.echo('Dropping database tables')
    db.reflect()
    db.drop_all()
