#!/usr/bin/python3
"""Sum of integers"""


def add_integer(a, b=98):
    """Adds two numbers
    Args:
    a - first number input
    b - second number input
    """
    if type(a) not in [int, float] or type(b) not in [int, float]:
        raise TypeError("a must be an integer or b must be an integer")
    return int(a) + int(b)
