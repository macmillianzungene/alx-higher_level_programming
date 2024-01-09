#!/usr/bin/python3
"""
This module provides a function to get a dictionary description of an object.
"""

def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization of an object.

    Args:
        obj: An instance of a Class.

    Returns:
        A dictionary description of the object.
    """
    return {key: value for key, value in obj.__dict__.items() if type(value) in [list, dict, str, int, bool]}

