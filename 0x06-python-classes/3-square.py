#!/usr/bin/python3
"""this is a square class to be defined"""


class Square:
    """this is a square class"""
    def __init__(self, size=0):
        self.__size = size
        if isinstance(size, int) is False:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        return self.__size ** 2
