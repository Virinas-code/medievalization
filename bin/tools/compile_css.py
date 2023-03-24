#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Medievalization

CSS compile tool
"""
import glob

if __name__ == "__main__":
    for directory in glob.glob("ui/**/css"):
        directives: list[str] = []

        for file in glob.glob(f"{directory}/*.css"):
            directives.append(f'@import url("/public/{file}");\n')

        with open(
            f"public/{directory}/styles.css",
            "w",
            encoding="utf-8",
        ) as compiled_file:
            compiled_file.writelines(directives)
