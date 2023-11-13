#!/usr/bin/python3
"""this is a module of base"""


class Base:
    """a base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """a class initiation function"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
