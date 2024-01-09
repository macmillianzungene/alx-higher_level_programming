#!/usr/bin/python3
"""
This module defines a function to generate Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's Triangle of n.

    Args:
        n (int): The number of rows in Pascal's Triangle.

    Returns:
        list: A list of lists representing Pascal's Triangle. Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        last_row = triangle[i - 1]
        row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
        row.append(1)
        triangle.append(row)

    return triangle

