#!/usr/bin/python3
"""Defines a name printing function"""


def say_my_name(first_name, last_name=""):
    """
    prints a string with the format "My name is <firstname> <lastname>".

    Args:
         first_name: The first name to print.
         last_name : The lastname to print. Defaults to an empty string.

    Raises:
         TypeError: If the first name or last name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("First name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("Last name must be a string")
    print("My name is {} {}".format(first_name, last_name))
