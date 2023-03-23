# -*- coding: utf-8 -*-
"""
Medievalization

i18n translations loader
"""
import json
import os

from modules.i18n.types import Translations


def load() -> Translations:
    """
    Load translations from files.

    :return Translations: A translations object.
    """
    translations: Translations = {}
    for directory in os.listdir("data/i18n/"):
        translations[directory] = {}

        for file in os.listdir(f"data/i18n/{directory}/"):
            with open(
                f"data/i18n/{directory}/{file}", encoding="utf-8"
            ) as file_object:
                translations[directory][file.split(".")[0]] = json.load(
                    file_object
                )
    return translations
