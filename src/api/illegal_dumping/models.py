import os
from sqlalchemy.sql import func
from src import db


class IllegalDumping(db.Model):

    __tablename__ = "illegal_dumping"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    vehicle = db.Column(db.String(1024), nullable=False)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, vehicle, license):
        self.vehicle = vehicle


if os.getenv("FLASK_ENV") == "development":
    from src import admin
    from src.api.illegal_dumping.admin import IllegalDumpingAdminView

    admin.add_view(IllegalDumpingAdminView(IllegalDumping, db.session))
