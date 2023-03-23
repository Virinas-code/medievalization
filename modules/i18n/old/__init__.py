# -*- coding: utf-8 -*-
"""
Medievalization

i18n module
"""
from typing import NamedTuple

from modules.i18n.load import load as load_trans
from modules.i18n.objected import objected


def load() -> NamedTuple:
    """
    Load translations.

    :return NamedTuple: The ``trans`` object.
    """
    return objected(load_trans())
