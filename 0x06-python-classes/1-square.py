#!/usr/bin/python3
"""
This is the "my_module" module.

The my_module module defines the Square class.
"""

class Square:
    """
    This is the Square class.
    
    The Square class defines a square with a private instance attribute size.
    """
    def __init__(self, size):
        """
        This is the constructor for Square class.
        
        The constructor instantiates a Square object with a given size.
        """
        self.__size = size

