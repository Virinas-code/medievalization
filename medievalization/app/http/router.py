#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Medievalization router.

Binds all routes.
"""
from flask import Flask
from ..controllers.main import route_main


def route(app: Flask) -> None:
    """
    Add routes to an app.

    :param Flask app: App to add routes to.
    """
    app.add_url_rule("/", view_func=route_main)
