#!/usr/bin/python3
"""load from json file inpython module"""
import json


def load_from_json_file(filename):
    """loads from a json file"""
    with open(filename, encoding="utf-8") as f:
        x = f.read()
        k = json.loads(x)
        return k
