#!/usr/bin/python3
"""
This module defines a function to append a line of text to a file,
after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing a specific string.

    Args:
        filename (str): The name of the file.
        search_string (str): The specific string to be searched in the file.
        new_string (str): The new string to be inserted into the file.

    Returns:
        None
    """
    with open(filename, 'r+') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if search_string in line:
                lines[i] = line + new_string
        f.seek(0)
        f.writelines(lines)

