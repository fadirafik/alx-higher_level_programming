#!/usr/bin/python3
"""save to json module"""
import json


def save_to_json_file(my_obj, filename):
    """save to ajson file"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
