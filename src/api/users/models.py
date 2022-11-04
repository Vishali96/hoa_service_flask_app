import os
from sqlalchemy.sql import func
from src import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


class User(db.Model, UserMixin):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)
    password = db.Column(db.String(300), nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email


if os.getenv("FLASK_ENV") == "development":
    from src import admin
    from src.api.users.admin import UsersAdminView

    admin.add_view(UsersAdminView(User, db.session))
