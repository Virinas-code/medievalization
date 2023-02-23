# -*- coding: utf-8 -*-
"""
Medievalization

Main server file
"""
import flask

server: flask.Flask = flask.Flask(
    "medievalization",
    static_url_path="/public/",
    static_folder="public",
    template_folder="app/views",
)
