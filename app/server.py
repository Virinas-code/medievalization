# -*- coding: utf-8 -*-
"""
Medievalization

Main server file
"""
import sys
import uuid
from typing import Any

import flask

from app.controllers.auth import auth_blueprint
from modules.i18n import load_trans

server: flask.Flask = flask.Flask(
    "medievalization",
    static_url_path="/public/",
    static_folder="public",
    template_folder="app/views",
)
server.secret_key = uuid.uuid4().hex


@server.context_processor
def inject_translations() -> dict[str, Any]:
    """
    Shared translation object.

    :return dict[str, Any]: Variables for Jinja templates.
    """
    print("inject", file=sys.stderr)
    return {"trans": load_trans()}


server.register_blueprint(auth_blueprint)


@server.route("/dev")
def test_route():
    """Test."""
    flask.session["i18n.language"] = "fr"
    return "OK"
