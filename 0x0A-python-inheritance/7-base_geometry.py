#!/usr/bin/python3
"""
base geometry module
"""


class BaseGeometry:
    """base geometry class"""

    def area(self):
        """returns the area of the object"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates the value"""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))

        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
