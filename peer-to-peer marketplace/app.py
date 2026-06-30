from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = "auth.login"

    # Register Blueprints
    from routes.auth_routes import auth
    from routes.product_routes import product

    app.register_blueprint(auth)
    app.register_blueprint(product)

    with app.app_context():
        db.create_all()

    return app