#!/usr/bin/python3
"""
This module contains a function add_integer that adds two numbers.

The function takes two parameters, a and b, which should be integers or floats.
If they are floats, they are casted to integers before addition.
If either of them is not an integer or float, a TypeError is raised.
"""

def add_integer(a, b=98):
    """
    Function to add two numbers after ensuring they are integers.

    Parameters:
    a: The first number. Must be an integer or float.
    b: The second number. Must be an integer or float. Defaults to 98.

    Returns:
    The sum of a and b, as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

