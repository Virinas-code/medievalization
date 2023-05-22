# -*- coding: utf-8 -*-
"""
Session System

Start server
"""
import lib.session_db as lib

server: lib.Server = lib.Server()

if __name__ == "__main__":
    server.main_loop()
