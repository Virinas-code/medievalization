# -*- coding: utf-8 -*-
"""
Session system

Decorator and function to interact with sessions
"""
import pickle
import socket
from typing import Any, Callable, Optional, ParamSpec
from uuid import UUID, uuid4

import tomllib
from flask import Response, session

Param = ParamSpec("Param")

with open("conf/session.toml", "rb") as file:
    conf: dict[str, Any] = tomllib.load(file)

connection: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect((conf["bind"]["address"], conf["bind"]["port"]))
connection.settimeout(32)


def get_session(uuid: UUID) -> dict[str, Any]:
    """
    Get a session.

    :param UUID uuid: Session ID.
    :return dict[str, Any]: Session data.
    """
    connection.send(pickle.dumps(("get", str(uuid))))
    return pickle.loads(connection.recv(1 << 16))


def set_session(uuid: UUID, value: dict[str, Any]) -> None:
    """
    Set a session data

    :param UUID uuid: Session ID
    :param dict[str, Any] value: Session data
    """
    connection.send(pickle.dumps(("set", (str(uuid), value))))
    assert pickle.loads(connection.recv(1 << 16)) == "OK", "Failed to set session"


def start_session(uuid: Optional[UUID] = None) -> UUID:
    """
    Start a session

    :param Optional[UUID] uuid: Session ID, defaults to None
    :return UUID: Session ID
    """
    safe_uuid: UUID = uuid or uuid4()
    connection.send(pickle.dumps(("login", str(safe_uuid))))
    assert pickle.loads(connection.recv(1 << 16)) == "OK", "Failed to start session"
    session["session.uuid"] = safe_uuid
    return safe_uuid


def pass_session(function: Callable[Param, Response]) -> Callable[Param, Response]:
    """
    Inject new session system.

    :param Callable[Param, Response] function: View function
    :return Callable[Param, Response]: Injected function
    """

    def wrapper(*args: Param.args, **kwargs: Param.kwargs) -> Response:
        """
        Wrapper for session factory.

        :return Response: Returned response
        """
        function_globals: dict[str, Any] = function.__globals__
        function_globals["safe_session"] = get_session(session["session.uuid"])

        answer: Response = function(*args, **kwargs)

        del function_globals["safe_session"]

        return answer

    return wrapper
