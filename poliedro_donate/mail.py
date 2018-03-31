import requests
from flask import render_template

from . import app
from .errors import MailerError

"""
Mailers should be used as classes: all configuration must be stored in app.config.
"""

_mailers = {}


def register_mailer(name, mailer):
    _mailers[name] = mailer


def get_mailer(name=None):
    if not name:
        name = app.config["APP_MAILER"]

    return _mailers[name]


class Mailer(object):
    def __init__(self):
        raise AssertionError("Mailers should not be instanced")

    @classmethod
    def send(cls, data, template_vars, plaintext_template, html_template=None, files=None):
        raise NotImplementedError


class MailgunMailer(Mailer):
    send_url = "https://api.mailgun.net/v3/{domain}/messages"

    @classmethod
    def send(cls, data, template_vars, plaintext_template, html_template=None, files=None):
        data["text"] = str(render_template(plaintext_template, **template_vars))
        if html_template:
            data["html"] = str(render_template(html_template, **template_vars))

        kwargs = {
            "auth": ("api", app.config["MAILGUN_API_KEY"]),
            "data": data
        }

        if files:
            kwargs["files"] = files

        r = requests.post(
            cls.send_url.format(app.config["MAILGUN_DOMAIN"]),
            **kwargs
        )

        if r.status_code != 200:
            raise MailerError(r.text)


register_mailer("mailgun", MailgunMailer)
