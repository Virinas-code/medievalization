# -*- coding: utf-8 -*-
"""
Medievalization

Register page
"""
from flask import Response, abort, request

from app.http.returns import redirect, render_template
from modules.auth import login as login_func


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
        return abort(501)
    return render_template("auth/register.html")
