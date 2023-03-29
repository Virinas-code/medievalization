# -*- coding: utf-8 -*-
"""
Medievalization

Main server file
"""
import uuid
from typing import Any

import flask

from app.controllers.auth import auth_blueprint
from modules.i18n import load_trans
from modules.i18n.languages import LANGUAGES

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
    # TODO: Store in variable for better performance (called all the time)
    return {"trans": load_trans(), "languages": LANGUAGES}


server.register_blueprint(auth_blueprint)
