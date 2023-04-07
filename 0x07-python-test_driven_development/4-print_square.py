#!/usr/bin/python3
"""Defines a square printing function"""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
    size (int): The length of the sides of the square.

    Raises:
    TypeError if size is not an integer.
    ValueError if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError(size must be an integer)
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size + '\n')
