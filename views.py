from flask import Blueprint
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        session["user"] = user
        flash(f"{user}, you have logged in successfully!", "info")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            user = session["user"]
            flash(f"{user}, you are already logged in!", "info")
            return redirect(url_for("user"))
        return render_template("login.html")

@views.route("/user", methods = ["POST", "GET"])
def user():
    loginid = None
    '''
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            loginid = request.form["loginid"]
            session["loginid"] = loginid
        else:
            if "loginid" in session:
                loginid = session["loginid"]

        return render_template("user.html", loginid = loginid)
    else:
    '''
    return render_template("user.html")

@views.route("/blog")
def blog():
    return render_template("blog.html")

@views.route("/games")
def games():
    return render_template("games.html")

@views.route("/merchandize")
def merchandize():
    return render_template("merchandize.html")

@views.route("/saved")
def saved():
    return render_template("saved.html")

@views.route("/settings")
def settings():
    return render_template("settings.html")

@views.route("/analytics")
def analytics():
    return render_template("analytics.html")

@views.route("/logout")
def logout():
    flash("You have been logged out successfully!", "info")
    session.pop("user", None)
    session.pop("loginid", None)

    return redirect(url_for("login"))
