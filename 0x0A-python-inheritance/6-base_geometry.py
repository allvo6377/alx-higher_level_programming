#!/usr/bin/python3
"""A module that creates an inherited class"""


class BaseGeometry:
    """A class that represents the base of geometry."""

    def area(self):
        """A public instance method that raises an Exception with the message,
        area() is not implemented."""
        raise Exception("area() is not implemented")
