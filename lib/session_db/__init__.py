# -*- coding: utf-8 -*-
"""
Medievalization

Session database system
"""
import pickle
import socket
import sys
import traceback
from typing import Any, cast
from uuid import UUID

import pretty_errors
import tomllib

pretty_errors.configure(
    display_arrow=True,
    display_link=True,
    display_locals=True,
    display_timestamp=True,
    display_trace_locals=True,
    lines_before=2,
    lines_after=2,
    trace_lines_after=2,
    trace_lines_before=2,
    link_color=pretty_errors.BRIGHT_BLUE,
    code_color=pretty_errors.WHITE,
)
pretty_errors.blacklist("~/.cache/pypoetry", "<frozen runpy>")

OK: bytes = pickle.dumps("OK")
ERROR: bytes = pickle.dumps("ERROR")

with open("conf/session.toml", "rb") as file:
    conf: dict[str, Any] = tomllib.load(file)


class Server:
    """Main socket server."""

    def __init__(
        self, host: str = conf["bind"]["host"], port: int = conf["bind"]["port"]
    ) -> None:
        """
        Start the session db server.

        :param str host: Host to run on.
        :param str port: Port to run on.
        """
        self.sessions: dict[UUID, dict[str, Any]] = {}

        self.socket: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((host, port))
        self.socket.listen(4)
        self.client: socket.socket = self.wait()

    def wait(self) -> socket.socket:
        """
        Wait for a client to connect.

        :return socket.socket: Client socket.
        """
        client: socket.socket
        address: socket._Address
        client, address = self.socket.accept()
        inet_address: tuple[str, str] = cast(tuple[str, str], address)
        print(f"Database started, client is {inet_address[0]}:{inet_address[1]}")
        return client

    def main_loop(self) -> None:
        """
        Main loop.

        Receive and process.
        """
        while True:
            data: bytes = self.client.recv(1 << 16)  # 16 Kb buffer
            try:
                self.client.send(self.process(data))
            except Exception as excepted:
                traceback.print_exception(excepted, file=sys.stderr)
                self.client.send(ERROR)

    def process(self, data: bytes) -> bytes:
        """
        Process data received.

        :param bytes data: Data received.
        :return bytes: Answer.
        """
        decoded: tuple[str, Any] = pickle.loads(data)
        print(decoded[0])
        if decoded[0] == "login":
            login_uuid: UUID = UUID(decoded[1])
            self.sessions[login_uuid] = {}
            return OK
        elif decoded[0] == "logout":
            logout_uuid: UUID = UUID(decoded[1])
            del self.sessions[logout_uuid]
            return OK
        elif decoded[0] == "get":
            get_uuid: UUID = UUID(decoded[1])
            return pickle.dumps(self.sessions[get_uuid])
        elif decoded[0] == "set":
            set_uuid: UUID = UUID(decoded[1][0])
            self.sessions[set_uuid] = decoded[1][1]
            return OK
        return ERROR
