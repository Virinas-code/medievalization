# -*- coding: utf-8 -*-
"""
Medievalization

Standardised functions
"""
from typing import Any, Callable, List, Union

import flask
from flask import Response, make_response
from jinja2.environment import Template

redirect: Callable[[str], Response] = lambda url: make_response(flask.redirect(url))


def render_template(
    template_name_or_list: Union[str, Template, List[str | Template]], **context: Any
) -> Response:
    """
    Render a template by name with the given context.

    :param Union[str, Template, List[str | Template]] template_name_or_list:
        The name of the template to render. If
        a list is given, the first name to exist will be rendered.
    :param Any context: The variables to make available in the template.
    :return Response: A valid Flask reponse.
    """
    return make_response(flask.render_template(template_name_or_list, **context))


def no_content() -> Response:
    """
    Return 204 - No Content.

    :return Response: An empty response.
    """
    return make_response(("", 204))
