# -*- coding: utf-8 -*-
"""
Medievalization

Better sessions
"""
import json
from typing import Any, Callable, TypeAlias, cast
from uuid import UUID, uuid4

from flask import Response, abort, request, session

Session: TypeAlias = dict[str, Any]
database: dict[UUID, dict[str, Any]] = {}


class View:
    """Access database."""

    def __init__(self, uuid: UUID):
        """
        Initialize view.

        :param UUID uuid: Safe session UUID.
        """
        self.uuid: UUID = uuid
        self._data: dict[str, Any] = self._load(uuid)

    @staticmethod
    def _load(uuid: UUID) -> dict[str, Any]:
        with open(f"data/http/sessions/{uuid.hex}") as file:
            return json.load(file)

    def _save(self) -> None:
        with open(f"data/http/sessions/{self.uuid.hex}", "w") as file:
            json.dump(self._data, file)

    def get(self, key: str) -> Any:
        """
        Get a value.

        :param str key: Key.
        :return Any: Value.
        """
        return self._data[key]

    def set(self, key: str, value: Any) -> None:
        """
        Set a value.

        :param str key: Key.
        :param Any value: Value.
        """
        self._data[key] = value
        return self._save()


def safe_session(session_id: str, remote_addr: str) -> Session:
    """
    Safer session,

    :param str session_id: UUID of the session.
    :param str remote_addr: IP for better safety.
    :return Session: The session.
    """
    uuid: UUID = UUID(session_id)
    if uuid not in database:
        abort(400)
    database_session: dict[str, Any] = database[uuid]
    if database_session["http.ip"] != remote_addr:
        del database[uuid]
        abort(400)
    return database_session


def session_factory(function: Callable[..., Response]) -> Callable[..., Response]:
    """
    Inject new session system.

    :param Callable[..., Response] function: View function
    :return Callable[..., Response]: Injected function
    """

    def wrapper(*args, **kwargs) -> Response:
        """
        Wrapper for session factory.

        :return Response: Returned response
        """
        function_globals: dict[str, Any] = function.__globals__
        function_globals["safe_session"] = safe_session(
            session["id"], cast(str, request.remote_addr)
        )

        answer: Response = function(*args, **kwargs)

        del function_globals["safe_session"]

        return answer

    return wrapper
