
__all__ = ('donations_bp', 'donation')

from flask import Blueprint, render_template
from .. import strings
from ..auth import requires_auth
from ..database import helpers
from ..database.models import Donation, User

donations_bp = Blueprint('donations', __name__)


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