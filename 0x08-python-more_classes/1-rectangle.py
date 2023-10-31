#!/usr/bin/python3
"""
the module for rectangle class
"""


class Rectangle:
    """a rectangle class"""

    def __init__(self, width=0, height=0):
        """ initialize a new rectangle

        args:
            width
            height
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """returns the width instance attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """returns the height instance attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
