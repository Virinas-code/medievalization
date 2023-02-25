# -*- coding: utf-8 -*-
"""
Medievalization

Login module
"""
import csv
from hashlib import sha512

from flask import session


def login(username: str, password: str) -> bool:
    """
    Login an user.

    :param str username: Username.
    :param str password: Password.
    :return bool: True if correct.
    """
    with open("test.csv", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=",", quotechar='"')
        passwords: list[list[str]] = list(reader)
    passwords_dict: dict[str, str] = dict(passwords)

    hashed: str = sha512(password.encode()).hexdigest()
    if passwords_dict[username] == hashed:
        session["auth.username"] = username
        return True
    return False


def signup(username: str, password: str, email: str) -> None:
    """
    Signup a new user.

    :param str username: Username.
    :param str password: Password.
    :param str email: Email for confirmation.
    """
