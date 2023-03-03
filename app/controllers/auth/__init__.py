# -*- coding: utf-8 -*-
"""
Medievalization

Auth blueprint
"""
from flask import Blueprint

from app.controllers.auth.oauth import done, handle, start

auth_blueprint = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth/",
)

auth_blueprint.add_url_rule("/oauth/", view_func=start)
auth_blueprint.add_url_rule(
    "/oauth/handle", methods=["POST", "GET"], view_func=handle
)
auth_blueprint.add_url_rule("/oauth/done", view_func=done)
