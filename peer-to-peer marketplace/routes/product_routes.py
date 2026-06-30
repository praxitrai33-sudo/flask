from flask import Blueprint, render_template
from flask_login import login_required

product = Blueprint("product", __name__)


@product.route("/")
def home():
    return render_template("index.html")


@product.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")