#!/usr/bin/python3
"""string to obj module"""
import json


def from_json_string(my_str):
    """decodes a json string to an object"""
    return  json.loads(my_str)
