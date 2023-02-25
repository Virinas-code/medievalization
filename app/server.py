# -*- coding: utf-8 -*-
"""
Medievalization

Main server file
"""
import flask

from app.controllers.auth import auth_blueprint

server: flask.Flask = flask.Flask(
    "medievalization",
    static_url_path="/public/",
    static_folder="public",
    template_folder="app/views",
)

server.register_blueprint(auth_blueprint)
