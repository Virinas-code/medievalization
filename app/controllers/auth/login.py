# -*- coding: utf-8 -*-
"""
Medievalization

Login page
"""
from flask import Response, abort, flash, request, url_for

from app.http.returns import redirect, render_template
from modules.auth import exists
from modules.auth import login as login_func
from modules.auth import signup
from modules.i18n import trans

FIELDS: tuple[str, str, str] = ("username", "mail", "password")


def login() -> Response:
    """
    Login page.

    /auth/login, methods GET and POST.

    :return Response: Login page or redirection if POST.
    """
    error: str = ""
    if request.method == "POST":
        if login_func(username=request.form["mail"], password=request.form["password"]):
            return redirect("/app")
        error = "Invalid credentials"
    return render_template("auth/login.html", error=error)


def register() -> Response:
    """
    Registering page.

    /auth/register, methods GET and POST.

    :return Response: Registering page or redirection if POST.
    """
    if request.method == "POST":
        if not all(k in request.form for k in FIELDS):
            print(request.form)
            return abort(400)
        if not all(request.form[k] is not None for k in FIELDS):
            flash("Please fill all the fields.")
            return render_template("auth/register")
        if exists(request.form["username"]):
            flash("An user already has this name.")
            return render_template("auth/register")
        signup(request.form["username"], request.form["password"], request.form["mail"])
        flash("Confirmation email sent.")
        return redirect(url_for("auth.login"))
    return render_template("auth/register.html")
