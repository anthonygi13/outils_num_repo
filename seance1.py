#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File : seance1.py
# Created by Anthony Giraudo at 08/10/2019

"""FIXME: INCOMPLET
"""

# Modules

import time
import getpass, socket
import os

# Functions

def username():
    return getpass.getuser()

def ordi():
    return socket.gethostname()

def date():
    return time.strftime("%y%m%d")

def fname(n):
    return "_".join([username(), ordi(), date()]) + ".txt"

def create_files():
    pass


# Main
if __name__ == "__main__":
    pass
