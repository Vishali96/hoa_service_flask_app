# views.py

from flask import Blueprint, render_template
from flask_login import login_required, current_user
from src.api.illegal_dumping.models import IllegalDumping

illegal_dumping_blueprint = Blueprint('illegal_dumping_blueprint', __name__)

@illegal_dumping_blueprint.route('/illegal-dumping')
@login_required
def illegal_dumping():
    vehicles = IllegalDumping.query.order_by(IllegalDumping.created_date).limit(5).all()
    return render_template('illegal_dumping.html', name=current_user.username, vehicles=vehicles)