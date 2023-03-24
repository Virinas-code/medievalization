# -*- coding: utf-8 -*-
"""
Medievalization

i18n main module
"""
from typing import NamedTuple

from modules.i18n.load import load
from modules.i18n.objected import objected


def load_trans() -> NamedTuple:
    """
    Load all translations.

    Returns the ``trans`` object.
    """
    return objected(load())
