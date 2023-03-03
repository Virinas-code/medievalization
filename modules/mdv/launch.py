# -*- coding: utf-8 -*-
"""
Medievalization

mdv build tools
"""
import importlib
import os
import sys
from pathlib import Path
from types import ModuleType

import click
from flask import Flask

from .build import build


@click.command()
def start() -> None:
    """Start server"""
    sys.path.append(os.path.abspath("./"))

    module: ModuleType = importlib.import_module("app.server")

    app: Flask = module.server
    app.run(
        "0.0.0.0",
        port=443,
        debug=True,
        ssl_context=("conf/ssl/v2/cert.crt", "conf/ssl/v2/key.key"),
    )


@click.command()
def clean() -> None:
    """Cleanup __pycache__"""
    for file in Path(".").rglob("*.py[co]"):
        file.unlink()

    for folder in Path(".").rglob("__pycache__"):
        folder.rmdir()


@click.group(invoke_without_command=True)
@click.pass_context
def launch(ctx: click.Context) -> None:
    """Build CSS and TypeScript."""
    if not ctx.invoked_subcommand:
        ctx.invoke(build)
        ctx.invoke(start)
        ctx.invoke(clean)


launch.add_command(start, "start")
launch.add_command(clean, "clean")
