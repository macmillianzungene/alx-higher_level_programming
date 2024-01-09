#!/usr/bin/python3
"""
This module provides a function to load an object from a file in JSON format.
"""

import json

def load_from_json_file(filename):
    """
    Creates an Object from a JSON file.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        The object that was stored in the file.
    """
    with open(filename, 'r') as f:
        return json.load(f)

