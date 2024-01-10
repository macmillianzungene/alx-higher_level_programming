#!/usr/bin/python3
"""
This module contains a function that multiplies two matrices using NumPy.

The function lazy_matrix_mul takes two matrices as input and returns their product.
"""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        numpy.ndarray: The product of the two matrices.

    Raises:
        TypeError: If m_a or m_b are not lists or if they contain non-integers/floats.
        ValueError: If m_a or m_b are not rectangular or if their dimensions don't match.
    """
    try:
        return np.matmul(m_a, m_b)
    except ValueError as e:
        raise ValueError("m_a and m_b can't be multiplied") from e
    except TypeError as e:
        raise TypeError("m_a and m_b should contain only integers or floats") from e

