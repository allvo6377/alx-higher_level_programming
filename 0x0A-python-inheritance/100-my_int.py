#!/usr/bin/python3
"""Defines a class MyInt that inherits from int"""


class MyInt(int):
    """A class that represents a rebel integer and inherits from int."""

    def __eq__(self, other):
        """A method that returns the opposite of the equality comparison,
        with another object."""
        return super().__ne__(other)

    def __ne__(self, other):
        """A method that returns the opposite of the inequality comparison,
        with another object."""
        return super().__eq__(other)
