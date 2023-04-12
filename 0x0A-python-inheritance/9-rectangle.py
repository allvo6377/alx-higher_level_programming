#!/usr/bin/python3
"""Module that returns string representation of rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that represents a rectangle and inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Instantiation with width and height.

        Args:
            width: An integer that represents the width of the rectangle.
            height: An integer that represents the height of the rectangle.

        Attributes:
            __width: A private attribute that stores the width of  rectangle.
            __height: A private attribute that stores the height of  rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """A method that returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """A method that returns a string representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
