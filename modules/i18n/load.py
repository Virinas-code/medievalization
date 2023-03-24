# -*- coding: utf-8 -*-
"""
Medievalization

i18n loader
"""
import os
from pathlib import Path
from typing import Iterator

from modules.i18n.file import File
from modules.i18n.types import AllKeys


def load() -> AllKeys:
    """
    Load all translations.

    :return AllKeys: ``trans`` as dict.
    """
    paths: Iterator[tuple[str, list[str], list[str]]] = iter(
        os.walk("data/languages/")
    )
    next(paths)  # Skip root

    keys: AllKeys = {}

    for folder, _, files in paths:
        folder_name: str = Path(folder).name
        keys[folder_name] = {}
        for file in files:
            keys[folder_name][Path(file).stem] = File(
                f"data/languages/{folder_name}/{file}"
            )

    return keys
