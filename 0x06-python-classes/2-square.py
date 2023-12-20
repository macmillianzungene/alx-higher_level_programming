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
    def __init__(self, size=0):
        """
        This is the constructor for Square class.
        
        The constructor instantiates a Square object with a given size.
        Size must be an integer and greater than or equal to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

