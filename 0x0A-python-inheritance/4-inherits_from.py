#!/usr/bin/python3
"""A module that valides whether or not an instance has been inherited"""


def inherits_from(obj, a_class):
    """Check if an object is an instance of a class that inherited from a specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        True if the object is an instance of a class that inherited from the specified class; otherwise False.
    """
    obj_class = type(obj)
    return issubclass(obj_class, a_class) and obj_class != a_class
