#!/usr/bin/python3
import json


def from_json_string(my_str):
    """decodes a json string to an object"""
    return  json.loads(my_str)
