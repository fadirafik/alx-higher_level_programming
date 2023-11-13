#!/usr/bin/python3
"""rectangle module"""
from models.base import Base


class Rectangle(Base):
    """a rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initiation of the class rectangle"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of width"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """Set/get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of height"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """sets/gets value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the value of x"""
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """sets/gets the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the value of y"""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """returns the area of the rectangle"""
        self.area = self.__height * self.__width
        return self.area

    def display(self):
        """displays the recrangle on the stdout"""
        if self.__height == 0 or self.__width == 0:
            print("")
            return
        [print("") for y in range(self.y)]
        for i in range(self.__height):
            for x in range(self.x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """sets the string of a class"""
        strin = "[{}] ({}) {}/{} - {}/{}".\
            format(type(self).__name__, self.id, self.__x,
                   self.__y, self.__width, self.__height)
        return strin

    def update(self, *args, **kwargs):
        """updates the initiation of a class call"""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for key, item in kwargs.items():
                if key == "id":
                    if item is None:
                        self.__initt__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = item
                elif key == "height":
                    self.__height = item
                elif key == "width":
                    self.__width = item
                elif key == "x":
                    self.__x = item
                elif key == "y":
                    self.__y = item

    def to_dictionary(self):
        """returns a dictionary from the instance attributes"""
        return {
            "id": self.id,
            "height": self.height,
            "width": self.width,
            "x": self.x,
            "y": self.y
        }
