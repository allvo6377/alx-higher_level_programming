#!/usr/bin/python3
"""Returns a list of attributes and methods of an object"""


def lookup(obj):
    """Returns a list of available attributes and methods of an object.

    Parameters:
    obj: any Python object

    Returns:
    a list of strings containing the names of attributes and methods of obj
    """
    return dir(obj)
