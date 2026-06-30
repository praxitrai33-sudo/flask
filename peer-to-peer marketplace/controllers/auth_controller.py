from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user

from app import db
from models.user import User


def register():

    if request.method == "POST":

        fullname = request.form["fullname"]

        email = request.form["email"]

        phone = request.form["phone"]

        course = request.form["course"]

        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if user:
            flash("Email already exists.")
            return redirect(url_for("auth.register"))

        new_user = User(
            fullname=fullname,
            email=email,
            phone=phone,
            course=course
        )

        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()

        flash("Registration Successful")

        return redirect(url_for("auth.login"))

    return render_template("register.html")


def login():

    if request.method == "POST":

        email = request.form["email"]

        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):

            login_user(user)

            flash("Welcome!")

            return redirect(url_for("product.dashboard"))

        flash("Invalid Email or Password")

    return render_template("login.html")


def logout():

    logout_user()

    flash("Logged Out")

    return redirect(url_for("auth.login"))