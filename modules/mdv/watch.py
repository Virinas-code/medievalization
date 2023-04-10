# -*- coding: utf-8 -*-
"""
Medievalization

mdv watch tools
"""
import time

import click
from watchdog.events import (
    EVENT_TYPE_CREATED,
    EVENT_TYPE_MODIFIED,
    EVENT_TYPE_MOVED,
    FileSystemEvent,
    FileSystemEventHandler,
)
from watchdog.observers import Observer
from watchdog.observers.api import BaseObserver

from modules.mdv.build import build_sources, build_styles

PATH: str = "ui/"
EVENTS: list[str] = [EVENT_TYPE_MOVED, EVENT_TYPE_CREATED, EVENT_TYPE_MODIFIED]


class BuildHandler(FileSystemEventHandler):
    """Handle file system events."""

    def __init__(self, action: bool | None):
        """
        Initialize handler.

        :param bool | None action: Sources or styles.
            True to watch TS, False to watch CSS.
            None to watch all.
        """
        self.action: bool | None = action

    def dispatch(self, event: FileSystemEvent) -> None:
        """
        Handle an event.

        :param FileSystemEvent event: Event.
        """
        if event.event_type not in EVENTS:
            return

        print(event.src_path)
        if self.action is None:
            build_sources()
            build_styles()
        elif self.action:
            build_sources()
        else:
            build_styles()


def observe(event_handler: bool | None) -> None:
    """
    Start watchdog.

    :param bool | None event_handler: Handler to use.
        See :py:class:`modules.mdv.watch.BuildHandler`.
    """
    handler: BuildHandler = BuildHandler(event_handler)
    observer: BaseObserver = Observer()
    observer.schedule(handler, PATH, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    return observer.join()


@click.command()
def watch_sources() -> None:
    """Watch TypeScript"""
    return observe(True)


@click.command()
def watch_styles() -> None:
    """Watch CSS"""
    return observe(False)


@click.group(invoke_without_command=True)
@click.pass_context
def watch(ctx: click.Context) -> None:
    """Watch CSS and TypeScript."""
    if not ctx.invoked_subcommand:
        observe(None)


watch.add_command(watch_sources, "sources")
watch.add_command(watch_styles, "styles")
