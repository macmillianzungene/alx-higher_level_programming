#!/usr/bin/python3
"""
This module provides a function to save an object to a file in JSON format.
"""

import json

def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation.

    Args:
        my_obj: The object to be written to the file.
        filename (str): The name of the file to write to.

    Returns:
        None
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)

