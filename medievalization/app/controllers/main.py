#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Medievalization / controller.

Shows debug screen.
"""
import flask


def route_main() -> flask.Response:
    """
    Route /.

    :return flask.Response: Response.
    """
    return flask.make_response(flask.render_template("app/views/loading.html"))
