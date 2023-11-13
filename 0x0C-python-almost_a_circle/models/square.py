#!/usr/bin/python3
"""square module"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """class of a square inheriting from recrangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """initiates the square object"""
        super().__init__(size, size, x, y)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """sets the size of the square object"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates an instance of a square object"""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def __str__(self):
        """Return the str representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    def to_dictionary(self):
        """returns a dictionary from the instance attributes"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
