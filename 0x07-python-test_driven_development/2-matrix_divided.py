#!/usr/bin/python3
"""Defines a module that divides matrix and divisor"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int/float): The number to divide the matrix elements by.

    Returns:
        list: A new matrix with all elements divided by div and rounded
        to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
        if each row of the matrix is not the same size, or if div is not
        a number (integer or float).
        ZeroDivisionError: If div is equal to 0.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if not all(isinstance(x, (int, float)) for row in matrix for x in row):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(x / div, 2) for x in row] for row in matrix]
