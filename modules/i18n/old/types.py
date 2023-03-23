# -*- coding: utf-8 -*-
"""
Medievalization

i18n types
"""
from __future__ import annotations

from typing import TypeAlias, Union

Key: TypeAlias = str
Value: TypeAlias = str

TranslationFile: TypeAlias = dict[Key, Union["TranslationFile", Value]]
Translations: TypeAlias = dict[Key, dict[Key, TranslationFile]]
