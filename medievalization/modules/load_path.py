#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Medievalization path module.

Load ressources path.
"""
import os


def load_path() -> None:
    """
    Move to data path.

    Must be called at the begining of the program.
    """
    environ_path: str = os.environ.get("MEDIEVALIZATION_PATH", "")
    if environ_path:
        os.chdir(environ_path)
    try:
        os.chdir("/usr/share/medievalization")
    except FileNotFoundError:
        os.chdir(os.path.expanduser("~/.local/share/medievalization"))
