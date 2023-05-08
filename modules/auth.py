# -*- coding: utf-8 -*-
"""
Medievalization

Login module
"""
from __future__ import annotations

import csv
import uuid
from typing import TYPE_CHECKING

from argon2 import PasswordHasher
from flask import session

HASHER: PasswordHasher = PasswordHasher()

if TYPE_CHECKING:
    from _csv import _reader as Reader  # pylint: disable=no-name-in-module
    from _csv import _writer as Writer  # pylint: disable=no-name-in-module

CONFIRM_FILE: str = "data/auth/confirm.csv"

with open("data/auth/users.csv", encoding="utf-8") as file:
    reader: Reader = csv.reader(file, delimiter=",", quotechar='"')
    passwords: list[list[str]] = list(reader)
passwords_dict: dict[str, str] = dict(passwords)


def login(username: str, password: str) -> bool:
    """
    Login an user.

    :param str username: Username.
    :param str password: Password.
    :return bool: True if correct.
    """
    if HASHER.verify(passwords_dict[username], password):
        session["auth.username"] = username
        return True
    return False


def signup(username: str, password: str, email: str) -> None:
    """
    Prepare to signup a new user.

    :param str username: Username.
    :param str password: Password.
    :param str email: Email for confirmation.
    """
    random_uuid: str = str(uuid.uuid4())
    with open(CONFIRM_FILE, "a", encoding="utf-8") as file:
        file.write(
            f"{username},{HASHER.hash(password.encode())},{email}," + f"{random_uuid}\n"
        )


def confirm(provided_uuid: str) -> bool:
    """
    Confirm signup of an user.

    :param str provided_uuid: Signup confirmation UUID.
    :return bool: True if worked.
    """
    # Get all confirmation data
    confirm_data: dict[str, tuple[str, str, str]] = {}
    with open(CONFIRM_FILE, encoding="utf-8") as file:
        reader: Reader = csv.reader(file, delimiter=",", quotechar='"')
        all_data: list[list[str]] = list(reader)
    for data in all_data:
        confirm_data[data[3]] = (data[0], data[1], data[2])

    # Check if user exists
    if provided_uuid not in confirm_data:
        return False

    # Add user to data
    with open("data/auth/users.csv", "a", encoding="utf-8") as file:
        writer: Writer = csv.writer(file, delimiter=",", quotechar='"')
        writer.writerow(confirm_data[provided_uuid])
    passwords_dict[confirm_data[provided_uuid][0]] = confirm_data[provided_uuid][2]

    # Remove row in csv lol
    del confirm_data[provided_uuid]
    with open(CONFIRM_FILE, encoding="utf-8") as file:
        removed_writer: Writer = csv.writer(file, delimiter=",", quotechar='"')
        for name, removed_data in confirm_data.items():
            removed_writer.writerow(
                (removed_data[0], removed_data[1], removed_data[2], name)
            )

    # All right, you're an user now
    return True


def exists(username: str) -> bool:
    """
    Check if an username is already used.

    :param str username: Username.
    :return bool: True if already used.
    """
    return username in passwords_dict.keys()
