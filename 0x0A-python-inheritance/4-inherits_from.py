#!/usr/bin/python3
"""
This module contains a function that checks if an object is an instance of a
class that inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Function to check if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if the object is an instance of a class that inherited (directly
        or indirectly) from the specified class ; otherwise False.
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)

