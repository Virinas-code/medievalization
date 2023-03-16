# -*- coding: utf-8 -*-
"""
Medievalization

Standardised functions
"""
from typing import Any, Callable, List, Union

import flask
from flask import Response, make_response
from jinja2.environment import Template
from typing_extensions import Protocol


class RenderTemplate(Protocol):
    """render_template annotation."""

    def __call__(
        self,
        template_name_or_list: Union[
            str, Template, List[Union[str, Template]]
        ],
        **context: Any
    ) -> Response:
        ...


redirect: Callable[[str], Response] = lambda url: make_response(
    flask.redirect(url)
)

render_template: RenderTemplate = (
    lambda template_name_or_list, **context: make_response(
        flask.render_template(template_name_or_list, **context)
    )
)
