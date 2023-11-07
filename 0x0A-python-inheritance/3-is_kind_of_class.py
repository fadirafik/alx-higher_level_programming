#!/usr/bin/python3
"""
is kind of class module
"""


def is_kind_of_class(obj, a_class):
    """checks if object is a subclass of a_class"""

    if type(obj) is a_class:
        return True
    if isinstance(obj, a_class):
        return True
    return False
