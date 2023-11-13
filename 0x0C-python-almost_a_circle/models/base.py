#!/usr/bin/python3
"""this is a module of base"""
import json


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

    @staticmethod    
    def to_json_string(list_dictionaries):
        """returns a json object of an instance dictionary"""
        if list_dictionaries is None:
            return "[]"
        else:
            json_string = json.dumps(list_dictionaries)
        return json_string
