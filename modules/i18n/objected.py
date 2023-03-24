# -*- coding: utf-8 -*-
"""
Medievalization

i18n objects
"""
from collections import namedtuple
from typing import NamedTuple, TypeAlias, Union

from modules.i18n.file import File

RecursiveDict: TypeAlias = dict[str, Union[str, "RecursiveDict"]]


def objected(input_dict: dict) -> NamedTuple:
    """
    Return a named tuple from a dict.

    :param dict input_dict: Input dict, might be nested.
    :return NamedTuple: Output named tuple.
    """
    translation_dict: type[NamedTuple] = namedtuple(
        "translation_dict", list(input_dict.keys())
    )
    values: dict[str, File | NamedTuple] = {}
    for key, value in input_dict.items():
        if isinstance(value, File):
            values[key] = value
        else:
            values[key] = objected(value)
    return translation_dict(**values)
