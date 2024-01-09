#!/usr/bin/python3
"""
This module provides a script to add all arguments to a Python list,
and then save them to a file in JSON format.
"""

import json
import sys
import os

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

if __name__ == "__main__":
    filename = "add_item.json"
    if not os.path.isfile(filename):
        save_to_json_file([], filename)
    my_list = load_from_json_file(filename)
    my_list.extend(sys.argv[1:])
    save_to_json_file(my_list, filename)

