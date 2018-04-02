from werkzeug.exceptions import NotFound

from poliedro_donate.validator import LOCATIONS

__all__ = ('donations_bp', 'donation')

from flask import Blueprint, render_template
from .. import strings
from ..auth import requires_auth
from ..database import helpers
from ..database.models import Donation, User

donations_bp = Blueprint('donations', __name__)


@donations_bp.route('/')
@requires_auth
def list_all():
    d = Donation.query.all()

    total = 0
    for donation in d:
        total += donation.amount

    return render_template('donations/list_all.html', donations=d, total=total)


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
    donation_sort_key = lambda d: d.pretty_id
    return render_template('donations/by_location.html', refs=refs, location=location,
                           donation_sort_key=donation_sort_key, dbhelpers=helpers, strings=strings)
