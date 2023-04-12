#!/usr/bin/python3
"""Defines a module that validates whether value is an integer"""


class BaseGeometry:
    """A class that represents the base of geometry."""

    def area(self):
        """A public instance method that raises an Exception with the message,
        area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A public instance method that validates value.

        Args:
            name: A string that represents the name of the value.
            value: An integer that represents the value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
