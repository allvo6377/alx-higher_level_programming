#!/usr/bin/python3
"""Defines a module that represents a rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that represents a rectangle and inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Instantiation with width and height.

        Args:
            width: An integer that represents the width of the rectangle.
            height: An integer that represents the height of the rectangle.

        Attributes:
            __width: A private attribute that stores the width of the rectangle.
            __height: A private attribute that stores the height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
