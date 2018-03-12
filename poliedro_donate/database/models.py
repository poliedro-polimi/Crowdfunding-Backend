__all__ = ("User", "Shirt", "Transaction", "Donation")

from .database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    listname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    lang = db.Column(db.String(2), default="en", nullable=False)
    donations = db.relationship("Donation", back_populates="reference")


class Shirt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.SmallInteger, nullable=False)
    size = db.Column(db.SmallInteger, nullable=False)
    donation_id = db.Column(db.Integer, db.ForeignKey("donation.id"), nullable=False)
    donation = db.relationship("Donation", back_populates="shirts")


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    payment_id = db.Column(db.String(30), nullable=False)
    state = db.Column(db.String(15), nullable=False)
    payment_obj = db.Column(db.Text, nullable=False)


class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)
    stretch_goal = db.Column(db.Integer, nullable=False)
    items = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    reference = db.relationship("User", back_populates="donations")
    shirts = db.relationship("Shirt", back_populates="donation")
    transaction_id = db.Column(db.Integer, db.ForeignKey("Transaction"), nullable=True)
    transaction = db.relationship("Donation")