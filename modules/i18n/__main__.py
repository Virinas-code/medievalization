#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Medievalization

i18n test
"""
from modules.i18n import load_trans

if __name__ == "__main__":
    print(load_trans())
    print(load_trans().auth.login.key)
