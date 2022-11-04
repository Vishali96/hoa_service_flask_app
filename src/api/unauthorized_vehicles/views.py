# views.py

from flask import Blueprint, render_template
from flask_login import login_required, current_user
from src.api.unauthorized_vehicles.models import UnauthorizedVehicles

unauthorized_vehicles_blueprint = Blueprint('unauthorized_vehicles_blueprint', __name__)

@unauthorized_vehicles_blueprint.route('/unauthorized-vehicles')
@login_required
def unauthorized_vehicles():
    # vehicles = UnauthorizedVehicles.query.order_by(UnauthorizedVehicles.created_date).limit(5).all()
    # vehicles = big_query_return()
    # print(type(vehicles[0]))
    vehicles = [
        {
            "id" : 1,
            "vehicle" : "https://cdn.searchenginejournal.com/wp-content/uploads/2019/07/the-essential-guide-to-using-images-legally-online-1520x800.png",
            "license": "abc123",
            "created_date" : "today"
        }, 
        {
            "id" : 2,
            "vehicle" : "https://cdn.searchenginejournal.com/wp-content/uploads/2019/07/the-essential-guide-to-using-images-legally-online-1520x800.png",
            "license": "xyz123",
            "created_date" : "yesterday"
        }
    ]
    return render_template('unauthorized_vehicles.html', name=current_user.username, vehicles=vehicles)