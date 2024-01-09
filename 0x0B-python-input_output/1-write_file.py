#!/usr/bin/python3
"""
This module contains a function that writes a string to a text file (UTF8) and returns the number of characters written.
"""

def write_file(filename="", text=""):
    """
    Function to write a string to a text file (UTF8) and return the number of characters written.

    Args:
        filename (str): The name of the file to be written to. Defaults to an empty string.
        text (str): The text to be written to the file. Defaults to an empty string.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)

