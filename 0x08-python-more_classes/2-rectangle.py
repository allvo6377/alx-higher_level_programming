#!/usr/bin/python3
"""A module that defines a clss rectangle"""


class Rectangle:
    """Defines a class rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes a new rectangle with a width and a height
        Args:
        width: an integer that represents object width
        height: an integer that represents object height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width attribute(private)"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width attribute value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Gets the height of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height of rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return 2 * (self.__width + self.__height)
