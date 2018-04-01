__all__ = ("User", "Shirt", "Transaction", "Donation")

import werkzeug
from .database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(10), nullable=False)
    lang = db.Column(db.String(2), default="en", nullable=False)

    def __repr__(self):
        return "<User {id}, firstname='{firstname}', lastname='{lastname}'>".format(id=self.id,
                                                                                    firstname=self.firstname,
                                                                                    lastname=self.lastname)


class Shirt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.SmallInteger, nullable=False)
    size = db.Column(db.SmallInteger, nullable=False)
    donation_id = db.Column(db.Integer, db.ForeignKey("donation.id"), nullable=False)
    donation = db.relationship("Donation",
                               backref=db.backref("shirts", lazy=True, uselist=True, cascade='all, delete-orphan',
                                                  single_parent=True))


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    payment_id = db.Column(db.String(30), nullable=True)
    payer_id = db.Column(db.String(30), nullable=True)
    state = db.Column(db.String(15), nullable=True)
    payment_obj = db.Column(db.Text, nullable=True)
    result_obj = db.Column(db.Text, nullable=True)


class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    stretch_goal = db.Column(db.Integer, nullable=False)
    items = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text, default="", nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    reference = db.relationship("User", backref=db.backref("donations", lazy=True, uselist=True))

    transaction_id = db.Column(db.Integer, db.ForeignKey("transaction.id"), nullable=True)
    transaction = db.relationship("Transaction", backref=db.backref("donation", lazy=True, uselist=False))

    @property
    def pretty_id(self):
        donation_id = "#D{}".format(self.id)

        if self.transaction:
            donation_id = "{}T{}".format(donation_id, self.transaction.id)

        return donation_id


class AdminUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    firstname = db.Column(db.String(100), nullable=True)
    lastname = db.Column(db.String(100), nullable=True)

    def __init__(self, username, password, firstname=None, lastname=None):
        self.username = username
        self.set_password(password)

        if firstname:
            self.firstname = firstname
        if lastname:
            self.lastname = lastname

    def set_password(self, password):
        self.password = werkzeug.generate_password_hash(password)

    def check_password(self, password):
        return werkzeug.check_password_hash(self.password, password)
