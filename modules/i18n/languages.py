# -*- coding: utf-8 -*-
"""
Medievalization

i18n supported lanugages
"""
from typing import NamedTuple


class Language(NamedTuple):
    """A supported language."""

    code: str
    """ISO code of the nation"""
    name: str
    """Language name"""
    language: str
    """Language used in translations"""


LANGUAGES: list[Language] = [
    Language("fr", "Français", "fr"),
    Language("gb", "English", "en"),
]
