# -*- coding: utf-8 -*-
"""
Medievalization

Easy-to-use, complete modding system
"""
import glob
from pathlib import Path

from modules.modloader.mod import Mod


class Modded:
    """A modded game manager."""

    def __init__(self, path: Path):
        """
        Initialize manager.

        Loads mods.

        :param Path path: Path to mods.
        """
        self.path: Path = path
        self.mods: list[Mod] = self._load_mods()

    def _load_mods(self) -> list[Mod]:
        """
        Load mods.

        :return list[Mod]: A list of mods.
        """
        for mod in self.path.iterdir():
            print(mod)
        return []  # TODO: Finish implementing
