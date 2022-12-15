#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Medievalization start script.

Only for debug.
"""
from . import init
from .app import server


def main() -> None:
    """Start server."""
    server.run("0.0.0.0", 80, debug=True)


if __name__ == "__main__":
    init()
    main()
