# -*- coding: utf-8 -*-
"""
Medievalization

i18n file object
"""
import json

from flask import session

from modules.i18n.types import Pairs


class File:
    """A translations file."""

    def __init__(self, file: str):
        """
        Generate translations.

        :param str file: File path.
        """
        with open(file, encoding="utf-8") as file_object:
            self.keys: Pairs = json.load(file_object)

    def __getattribute__(self, __name: str) -> str:
        """
        Get a translation key.

        :param str __name: Key name.
        :return str: Translated value.
        """
        if __name == "keys":
            return object.__getattribute__(self, __name)
        return self.keys.get(__name, {"en": "ERR500"}).get(
            session.get("i18n.language", "en"), "ERR500"
        )
