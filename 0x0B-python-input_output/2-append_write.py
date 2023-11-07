#!/usr/bin/python3
"""append write file module"""


def append_write(filename="", text=""):
    """writes a given text to a file"""
    with open(filename, "a", encoding="utf-8") as fl:
        a = fl.write(text)
        return a
