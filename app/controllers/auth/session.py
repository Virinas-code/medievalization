# -*- coding: utf-8 -*-
"""
Medievalization

Game session system
"""
from uuid import UUID

from flask import Response, abort, request

from modules.auth import login


def auth() -> Response:
    """
    Authenticate to your session.

    :return Response: /auth
    """
    if login(request.form["username"], request.form["password"]):
        return abort(204)
    return abort(401)


def validate() -> Response:
    """
    Validate a session key.

    :return Response: /validate
    """
