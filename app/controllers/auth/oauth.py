# -*- coding: utf-8 -*-
"""
Medievalization

Google OAuth
"""
from flask import Response, request, url_for

from app.http.returns import redirect, render_template
from modules.oauth import GoogleAuth

auth_flow: GoogleAuth = GoogleAuth()


def start() -> Response:
    """
    Start OAuth flow.

    :return Response: Redirect to authorization URL.
    """
    redirection: str = auth_flow.get_authorization_url(
        url_for("auth.handle", _external=True)
    )
    if redirection:
        return redirect(redirection)
    return redirect("/auth/oauth/done")


def handle() -> Response:
    """
    Handle OAuth response.

    :return Response: Redirect to /oauth/done.
    """
    print(request.values["code"])
    auth_flow.get_credentials(request.values["code"])
    return redirect("/auth/oauth/done")


def done() -> Response:
    """
    Handle OAuth done.

    :return Response: OAuth done page.
    """
    return render_template("oauth.html")
