import os
from sqlalchemy.sql import func
from src import db


class UnauthorizedVehicles(db.Model):

    __tablename__ = "unauthorized_vehicles"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    vehicle = db.Column(db.String(1024), nullable=False)
    license = db.Column(db.String(128), nullable=False)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, vehicle, license):
        self.vehicle = vehicle
        self.license = license


if os.getenv("FLASK_ENV") == "development":
    from src import admin
    from src.api.unauthorized_vehicles.admin import UnauthorizedVehiclesAdminView

    admin.add_view(UnauthorizedVehiclesAdminView(UnauthorizedVehicles, db.session))
