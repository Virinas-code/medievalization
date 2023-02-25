# -*- coding: utf-8 -*-
"""
Medievalization

Login page
"""
from flask import Response, make_response, redirect, render_template, request


def login() -> Response:
    """
    Login page.

    /auth/login, methods GET and POST.

    :return Response: Login page or redirection if POST.
    """
    if request.method == "POST":
        return make_response(redirect("/"))
    return make_response(render_template("login.html"))
