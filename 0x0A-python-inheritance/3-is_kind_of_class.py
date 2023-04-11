#!/usr/bin/python3
"""A module that checks whether an instance is from an inherited class"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of a specified class,
    or any of its subclasses.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        True if the object is an instance of the specified class or any of,
        its subclasses; otherwise False.
    """
    return isinstance(obj, a_class)
