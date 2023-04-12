#!/usr/bin/python3
"""Defines rectangle as a square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that represents a square and inherits from Rectangle."""

    def __init__(self, size):
        """Instantiation with size.

        Args:
            size: An integer that represents the size of the square.

        Attributes:
            __size: A private attribute that stores the size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """A method that returns the area of the square."""
        return self.__size ** 2
