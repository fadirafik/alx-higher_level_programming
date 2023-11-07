#!/usr/bin/python3
"""to json module"""
import json


def to_json_string(my_obj):
    """returns a json object"""
    a = json.dumps(my_obj)
    return a
