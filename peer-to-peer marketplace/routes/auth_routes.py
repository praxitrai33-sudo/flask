from flask import Blueprint

from controllers.auth_controller import register, login, logout

auth = Blueprint("auth", __name__)


auth.route("/register", methods=["GET", "POST"])(register)

auth.route("/login", methods=["GET", "POST"])(login)

auth.route("/logout")(logout)