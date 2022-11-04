from src import db
from src.api.users.models import User
from werkzeug.security import generate_password_hash

def get_all_users():
    return User.query.all()


def get_user_by_id(user_id):
    return User.query.filter_by(id=user_id).first()


def get_user_by_email(email):
    return User.query.filter_by(email=email).first()


def add_user(username, email, password):
    user = User(username=username, email=email, password=generate_password_hash(password, method='sha256'))
    db.session.add(user)
    db.session.commit()
    return user


def update_user(user, username, email, password):
    user.username = username
    user.email = email
    user.password = generate_password_hash(password, method='sha256')
    db.session.commit()
    return user


def delete_user(user):
    db.session.delete(user)
    db.session.commit()
    return user
