# -*- coding: utf-8 -*-
"""
Medievalization

i18n types
"""
from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    from modules.i18n.file import File

TranslatedKey: TypeAlias = dict[str, str]
Pairs: TypeAlias = dict[str, TranslatedKey]
AllKeys: TypeAlias = "dict[str, dict[str, File]]"
