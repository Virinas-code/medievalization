# -*- coding: utf-8 -*-
"""
Medievalization

mdv build tools
"""
import glob
import os

import click

GENERATED: str = "/* MDV: This file was automatically generated. */\n\n"


def build_sources() -> None:
    """Build TypeScript"""
    os.chdir("ui")
    os.system("tsc --build --pretty --verbose")
    os.chdir("..")


build_sources_command: click.Command = click.command(build_sources)


def build_styles() -> None:
    """Build CSS"""
    # Copy files
    for file in glob.glob("ui/**/css/*.css"):
        directory_path: str = os.path.dirname("public/" + file)
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

        with open(file, encoding="utf-8") as file_wrapper:
            with open(f"public/{file}", "w", encoding="utf-8") as new_file:
                new_file.write(GENERATED)
                new_file.write(file_wrapper.read())

    # Make compiled files
    for directory in glob.glob("ui/**/css"):
        directives: list[str] = [GENERATED]

        for file in glob.glob(f"{directory}/*.css"):
            directives.append(f'@import url("/public/{file}");\n')

        with open(
            f"public/{directory}/styles.css",
            "w",
            encoding="utf-8",
        ) as compiled_file:
            compiled_file.writelines(directives)


build_styles_command: click.Command = click.command(build_styles)


@click.group(invoke_without_command=True)
@click.pass_context
def build(ctx: click.Context) -> None:
    """Build CSS and TypeScript."""
    if not ctx.invoked_subcommand:
        build_sources()
        build_styles()


build.add_command(build_sources_command, "sources")
build.add_command(build_styles_command, "styles")
