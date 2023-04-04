#!/usr/bin/python3
"""Defines a function that multiplies two matrices"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Args:
        m_a (list): A list of lists of integers or floats.
        m_b (list): A list of lists of integers or floats.

    Returns:
        list: A new matrix that is the result of multiplying m_a and m_b.

    Raises:
        TypeError: If m_a or m_b is not a list, if m_a or m_b is not a,
        list of lists,
        if one element of those lists of lists is not an integer or a float,
        or if m_a or m_b is not a rectangle,
        (all rows should be of the same size).
        ValueError: If m_a or m_b is empty,
        or if m_a and m_b can't be multiplied.
    """
    # Check if m_a and m_b are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Check if m_a and m_b are lists of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # Check if m_a and m_b are not empty
    if not any(m_a) or not any(m_b):
        raise ValueError("m_a can't be empty" if not any(m_a)
                         else "m_b can't be empty")

    # Check if all elements of m_a and m_b are integers or floats
    if not all(isinstance(x, (int, float)) for row in m_a for x in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(x, (int, float)) for row in m_b for x in row):
        raise TypeError("m_b should contain only integers or floats")

    # Check if each row of m_a and m_b is the same size
    row_length_m_a = len(m_a[0])
    if not all(len(row) == row_length_m_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    row_length_m_b = len(m_b[0])
    if not all(len(row) == row_length_m_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    """
    Check if the number of columns in the first matrix is equal to the,
    number of rows in the second matrix
    """
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Multiply matrices
    result = [[sum(a * b for a, b in zip(row_m_a, col_m_b)) for col_m_b in
              zip(*m_b)] for row_m_a in m_a]
    return result
