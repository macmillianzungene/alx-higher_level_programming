#!/usr/bin/python3
"""
This module contains a function that returns an object (Python data structure) represented by a JSON string.
"""

def from_json_string(my_str):
    """
    Function to return an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): The JSON string to be deserialized.

    Returns:
        obj: The Python data structure represented by the JSON string.
    """
    return eval(my_str)

