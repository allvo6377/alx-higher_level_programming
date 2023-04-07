#!/usr/bin/python3
"""Defines a function that multiplies two matrices using numpy module"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using the numpy module.
    Args:
        m_a (list): A list of lists of integers or floats.
        m_b (list): A list of lists of integers or floats.
    Returns:
        list: A new matrix that is the result of multiplying m_a and m_b.
    """
    # Convert m_a and m_b to numpy arrays
    a = np.array(m_a)
    b = np.array(m_b)

    # Perform matrix multiplication
    result = np.dot(a, b)

    # Convert the result to a list of lists and return it
    return result.tolist()
