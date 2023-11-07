#!/usr/bin/python3
"""write file module"""


def write_file(filename="", text=""):
    """writes a given text to a file"""
    with open(filename, "w", encoding="utf-8") as fl:
        a = fl.write(text)
        return a
