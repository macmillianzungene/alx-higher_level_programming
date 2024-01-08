#!/usr/bin/python3
"""
This module contains a function that returns the list of available attributes
and methods of an object.
"""


def lookup(obj):
    """
    Function to return the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of the names of the available attributes and methods of the object.
    """
    return dir(obj)

