#!/usr/bin/python3
"""Defines a Python dictionary"""


def class_to_json(obj):
    """Return the dictionary"""
    return obj.__dict__
