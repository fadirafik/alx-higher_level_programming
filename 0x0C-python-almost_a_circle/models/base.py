#!/usr/bin/python3
"""this is a module of base"""
import json
import csv


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
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates an instance from a dictionary"""
        dummy = cls(0, 0, 0, 0)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """loads a file to a class"""
        x = cls.__name__ + ".json"
        newlis = []
        try:
            with open(x, "r") as fil:
                instance = Base.from_json_string(fil.read())
            return [cls.create(**d) for d in instance]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """write the listobj to a csv file"""
        filen = cls.__name__ + ".csv"
        with open(filen, "w", newline="") as fil:
            if list_objs is None or list_objs == []:
                fil.write([])
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(fil, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """loads from a csv file to an objects"""
        filen = cls.__name__ + ".csv"
        try:
            with open(filen, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_di = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_di = [dict([k, int(v)] for k, v in d.items())
                           for d in list_di]
                return [cls.create(**d) for d in list_di]
        except IOError:
            return []
