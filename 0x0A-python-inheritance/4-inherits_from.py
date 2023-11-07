#!/usr/bin/python3
"""
inherits from module
"""


def inherits_from(obj, a_class):
    """checks if obj inherits from a_class"""
    if type(obj) is a_class:
        return False
    if isinstance(obj, a_class):
        return True
    return False
