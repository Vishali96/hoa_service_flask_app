# auth.py

from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from src import db
from src.api.users.models import User

auth_blueprint = Blueprint('auth_blueprint', __name__)

@auth_blueprint.route('/login')
def login():
    return render_template('index.html')

@auth_blueprint.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    if not user or not check_password_hash(user.password, password): 
        flash('Please check your login details and try again.')
        return redirect(url_for('auth_blueprint.login')) # if user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect("/unauthorized-vehicles")

# @auth_blueprint.route('/profile')
# @login_required
# def profile():
#     return render_template('profile.html', name=current_user.username)

@auth_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('index.html')