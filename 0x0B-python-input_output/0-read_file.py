#!/usr/bin/python3
""""
read file module
"""


def read_file(filename=""):
    """prints the contents of a file"""
    with open(filename, encoding="utf-8") as fle:
        print(fle.read(), end="")
