# -*- coding: utf-8 -*-
"""
Medievalization

Standardised functions
"""
from typing import Callable

import flask
from flask import Response, make_response

redirect: Callable[[str], Response] = lambda url: make_response(
    flask.redirect(url)
)

render_template: Callable[[str], Response] = lambda path: make_response(
    flask.render_template(path)
)
