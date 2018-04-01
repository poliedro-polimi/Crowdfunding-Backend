__all__ = ('main', 'initdb', 'cleardb', 'adduser', 'deluser', 'passwd')

import click, getpass
from socket import gethostname

from poliedro_donate.database.models import AdminUser

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


@app.cli.command()
@click.argument("username")
@click.argument("firstname", required=False)
@click.argument("lastname", required=False)
@click.argument("password", required=False)
@commit_on_success
def adduser(username, firstname=None, lastname=None, password=None):
    """Create new admin user."""
    if not password:
        password = getpass.getpass('Password: ')
    u = AdminUser(username, password, firstname, lastname)
    db.session.add(u)


@app.cli.command()
@click.argument("username")
@commit_on_success
def deluser(username):
    """Delete admin user."""
    q = AdminUser.query.filter_by(username=username)

    if q.count() <= 0:
        raise ValueError("User does not exist")

    u = q[0]

    db.session.delete(u)


@app.cli.command()
@click.argument("username")
@click.argument("password", required=False)
@commit_on_success
def passwd(username, password=None):
    """Change admin user password."""
    if not password:
        password = getpass.getpass('New password: ')
    q = AdminUser.query.filter_by(username=username)

    if q.count() <= 0:
        raise ValueError("User does not exist")

    u = q[0]
    u.set_password(password)
