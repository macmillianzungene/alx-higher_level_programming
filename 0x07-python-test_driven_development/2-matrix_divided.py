#!/usr/bin/python3
"""
This module contains a function that divides all elements of a matrix.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number and returns a new matrix.

    Parameters:
    matrix (list of lists): The matrix to be divided.
    div (int or float): The number by which to divide the matrix elements.

    Returns:
    list of lists: A new matrix with all elements divided by div, rounded to 2 decimal places.
    """

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix) or not all(isinstance(item, (int, float)) for row in matrix for item in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(item / div, 2) for item in row] for row in matrix]

