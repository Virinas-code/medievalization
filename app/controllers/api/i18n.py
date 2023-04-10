# -*- coding: utf-8 -*-
"""
Medievalization

i18n set language controller
"""
from flask import Response, abort, session

from app.http.returns import no_content
from modules.i18n.languages import LANGUAGES


def set_language(language: str) -> Response:
    """
    Set i18n language.

    Route /api/i18n/<string:language>.

    :param str language: New session language.
    :return Response: 204.
    """
    for language_item in LANGUAGES:
        if language_item.language == language:
            session["i18n.language"] = language
            return no_content()
    return abort(400)
