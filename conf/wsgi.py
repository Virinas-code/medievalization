#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Medievalization WSGI script.

Used for mod_wsgi.
"""
from medievalization import init
from medievalization.app import server as application

init()

print(application)  # PLS Don't kill me
