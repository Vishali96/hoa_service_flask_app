import os

from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from werkzeug.middleware.proxy_fix import ProxyFix

# instantiate the extensions
db = SQLAlchemy()
admin = Admin(template_mode="bootstrap3")
login_manager = LoginManager()


def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__, static_url_path='/static')
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1)

    # set config
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)
    if os.getenv("FLASK_ENV") == "development":
        admin.init_app(app)

    login_manager.login_view = 'auth_blueprint.login'
    login_manager.init_app(app)

    # register api
    from src.api import api

    api.init_app(app)

    from src.api.users.auth import auth_blueprint
    app.register_blueprint(auth_blueprint)

    from src.api.unauthorized_vehicles.views import unauthorized_vehicles_blueprint
    app.register_blueprint(unauthorized_vehicles_blueprint)

    from src.api.illegal_dumping.views import illegal_dumping_blueprint
    app.register_blueprint(illegal_dumping_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
