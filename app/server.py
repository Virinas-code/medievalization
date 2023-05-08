# -*- coding: utf-8 -*-
"""
Medievalization

Main server file
"""
import uuid
from typing import Any

import flask

from app.controllers.api import api_blueprint
from app.controllers.auth import auth_blueprint
from app.http.error import handler as error_handler
from modules.i18n import load_trans
from modules.i18n.languages import LANGUAGES
from modules.logs import setup as setup_logs

server: flask.Flask = flask.Flask(
    "medievalization",
    static_url_path="/public/",
    static_folder="public",
    template_folder="app/views",
)
setup_logs(server)
server.secret_key = uuid.uuid4().hex


@server.context_processor
def inject_translations() -> dict[str, Any]:
    """
    Shared translation object.

    :return dict[str, Any]: Variables for Jinja templates.
    """
    return {
        "trans": load_trans(),
        "languages": LANGUAGES,
        "current_language": flask.session.get("i18n.language", "en"),
    }


server.register_error_handler(Exception, error_handler)

server.register_blueprint(auth_blueprint)
server.register_blueprint(api_blueprint)
