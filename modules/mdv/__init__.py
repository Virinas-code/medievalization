# -*- coding: utf-8 -*-
"""
Medievalization

mdv main script
"""
import click

from .build import build
from .launch import launch
from .watch import watch


@click.group()
def entry_point():
    """Entry point for all commands."""


entry_point.add_command(build, "build")
entry_point.add_command(launch, "launch")
entry_point.add_command(watch, "watch")
