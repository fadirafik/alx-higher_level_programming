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

    @classmethod
    def save_to_file(cls, list_obj):
        """adds the json object to a file"""
        x = cls.__name__
        x += ".json"
        newlis = []
        with open(x, "w") as fil:
            if list_obj is None:
                file.write("[]")
            else:
                for ls in list_obj:
                    newlis.append(ls.to_dictionary())
                s = Base.to_json_string(newlis)
                fil.write(s)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the json string representation"""
        return json.loads(json_string)
