#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Medievalization

Launch server
"""
import importlib
import os
import sys
from types import ModuleType

from flask import Flask

sys.path.append(os.path.abspath("./"))

module: ModuleType = importlib.import_module("app.server")

if __name__ == "__main__":
    app: Flask = module.server
    app.run("localhost", port=8080, debug=True)
