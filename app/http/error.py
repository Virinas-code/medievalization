# -*- coding: utf-8 -*-
"""
Medievalization

Error handler
"""
from traceback import format_exception

from flask import abort
from werkzeug.exceptions import HTTPException

from app.http.returns import Response, make_response, render_template


def handler(exception: Exception) -> Response:
    """
    Handles errors

    :param Exception exception: Handled exception.
    :return Response: Error page.
    """
    if not isinstance(exception, HTTPException):
        return abort(500, "Unknwon error")
    return make_response(
        render_template(
            "http/error.html", error=exception, exception=format_exception(exception)
        ),
        exception.code or 500,
    )
