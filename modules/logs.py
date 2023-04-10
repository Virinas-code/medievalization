# -*- coding: utf-8 -*-
"""
Medievalization

Logs module using Rich
"""
import logging.config

import rich
from flask import Flask
from flask.logging import default_handler
from rich.logging import RichHandler


def setup(server: Flask) -> None:
    """
    Setup new logs.

    Register Rich logger in Flask.

    :param Flask server: Current app.
    """
    server.logger.removeHandler(default_handler)
    server.logger.addHandler(RichHandler())
    logging.getLogger("wsgi").addHandler(RichHandler())


def init() -> None:
    """
    Init logs format.

    Uses logging module.
    """
    wsgi_logger: logging.Logger = logging.getLogger("wsgi")
