#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Medievalization

mdv build tool
"""
import logging

import click
import coloredlogs
import verboselogs as logs

coloredlogs.install()
logger: logs.VerboseLogger = logs.VerboseLogger("mdv", level=logging.NOTSET)


@click.group
def build() -> None:
    pass


@click.command
def build_sources() -> None:
    print("ts stuff")


build.add_command(build_sources, "sources")

if __name__ == "__main__":
    build()
