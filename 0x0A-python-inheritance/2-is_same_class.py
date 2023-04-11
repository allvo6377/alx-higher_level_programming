#!/usr/bin/python3
"""A function that checks whether or not two objects instances are the same"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        True if the object is exactly an instance of the specified,
        class; otherwise False.
    """
    obj_class = type(obj)
    if obj_class == a_class:
        return True
    else:
        return False
