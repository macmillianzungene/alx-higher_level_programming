#!/usr/bin/python3
"""
This module is used to demonstrate how to add a new attribute to an object.
"""


def add_attribute(obj, attr, value):
    """
    This function adds a new attribute to an object if it's possible.
    If the object can't have new attributes, it raises a TypeError exception.

    Args:
        obj: The object to which the attribute should be added.
        attr (str): The name of the attribute to be added.
        value: The value of the attribute to be added.

    Raises:
        TypeError: If the attribute cannot be added to the object.
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")

