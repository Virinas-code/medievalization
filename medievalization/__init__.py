#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Medievalization main module.

Contains init stuff.
"""
from .modules.load_path import load_path


def init() -> None:
    """
    Initialize server.

    Modules:
     - load_path
    """
    load_path()
