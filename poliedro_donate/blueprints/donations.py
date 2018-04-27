__all__ = ('donations_bp', 'donation')

from collections import OrderedDict
from werkzeug.exceptions import NotFound
from flask import Blueprint, render_template

from .. import strings, app
from ..auth import requires_auth
from ..database import helpers
from ..database.models import Donation, User, Transaction
from ..validator import LOCATIONS, STRETCH_GOAL_PRICES

donations_bp = Blueprint('donations', __name__)


@donations_bp.route('/')
@requires_auth
def list_all():
    costs = 0
    d = Donation.query.all()

    total = 0
    fees = 0
    for donation in d:
        if donation.transaction.state == 'approved':
            total += donation.amount
            costs += app.config["APP_SG_COSTS"][donation.stretch_goal] * donation.items
            fees += app.config.get("PAYPAL_STATIC_FEE", 0) + donation.amount * app.config.get("PAYPAL_FEE", 0)

    remaining = total - costs - fees
    total, costs, fees, remaining = round(total, 2), round(costs, 2), round(fees, 2), round(remaining, 2)
    total, costs, fees, remaining = "{:0.2f}".format(total), "{:0.2f}".format(costs), "{:0.2f}".format(
        fees), "{:0.2f}".format(remaining),

    return render_template('donations/list_all.html', donations=d, total=total, costs=costs, fees=fees,
                           remaining=remaining)


@donations_bp.route('/D<int:d_id>T<int:t_id>')
@donations_bp.route('/D<int:d_id>T<int:t_id>/')
@requires_auth
def donation(d_id, t_id):
    d = Donation.query.filter_by(id=d_id, transaction_id=t_id).first_or_404()
    return render_template('donations/donation.html', donation=d, dbhelpers=helpers, strings=strings)


@donations_bp.route('/reference/<int:r_id>')
@donations_bp.route('/reference/<int:r_id>/')
@requires_auth
def reference(r_id):
    r = User.query.filter_by(id=r_id).first_or_404()
    return render_template('donations/reference.html', reference=r)


@donations_bp.route('/by_location/<location>')
@donations_bp.route('/by_location/<location>/')
@requires_auth
def by_location(location):
    if location not in LOCATIONS:
        raise NotFound()

    refs = User.query.filter_by(location=location).order_by(User.lastname).all()
    donation_sort_key = lambda d: d.id
    return render_template('donations/by_location.html', refs=refs, location=location,
                           donation_sort_key=donation_sort_key, dbhelpers=helpers, strings=strings)


@donations_bp.route('/by_location/<location>/labels')
@donations_bp.route('/by_location/<location>/labels/')
@requires_auth
def print_labels(location):
    if location not in LOCATIONS:
        raise NotFound()

    refs = User.query.filter_by(location=location).order_by(User.lastname).all()
    donation_sort_key = lambda d: d.id
    return render_template('donations/print_labels.html', refs=refs, location=location,
                           donation_sort_key=donation_sort_key, dbhelpers=helpers, strings=strings)


@donations_bp.route('/to_order')
@donations_bp.route('/to_order/')
@requires_auth
def to_order():
    transactions = Transaction.query.filter_by(state='approved')
    shirts = []
    stretch_goals = [0] * len(STRETCH_GOAL_PRICES)

    for transaction in transactions:
        if transaction.donation.stretch_goal > 0:
            stretch_goals[transaction.donation.stretch_goal] += transaction.donation.items

        if transaction.donation.stretch_goal == 3:
            shirts += transaction.donation.shirts

    # Count gadgets for each stretch goal
    for i in range(len(stretch_goals)):
        stretch_goals[i] += sum(stretch_goals[i + 1:])

    return render_template('donations/to_order.html', stretch_goals=stretch_goals, shirts=shirts, dbhelpers=helpers,
                           strings=strings)
