# -*- coding: utf-8 -*-
"""
Medievalization

Internal API blueprint
"""
from flask import Blueprint

from app.controllers.api.i18n import set_language

api_blueprint = Blueprint(
    "api",
    __name__,
    url_prefix="/api/",
)

api_blueprint.add_url_rule("/i18n/<string:language>", view_func=set_language)
