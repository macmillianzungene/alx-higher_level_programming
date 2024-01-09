#!/usr/bin/python3
"""
This module contains a function that reads a text file (UTF8) and prints it to stdout.
"""

def read_file(filename=""):
    """
    Function to read a text file (UTF8) and print its contents to stdout.

    Args:
        filename (str): The name of the file to be read. Defaults to an empty string.

    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read())

