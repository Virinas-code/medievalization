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
    app.run(
        "0.0.0.0",
        port=443,
        debug=True,
        ssl_context=("conf/ssl/v2/cert.crt", "conf/ssl/v2/key.key"),
    )
