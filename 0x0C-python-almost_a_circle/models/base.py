#!/usr/bin/python3
"""A base module for Other classes in this project."""


class Base:
    """A base class for all other classes in this project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """A class constructor that initializes the id attribute."""

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
