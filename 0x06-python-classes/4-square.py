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
        self.size = size

    @property
    def size(self):
        """
        This is the getter method for size.
        
        It returns the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This is the setter method for size.
        
        It sets the size of the square after validating the value.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        This method calculates the area of the square.
        
        It returns the area of the square which is size squared.
        """
        return self.__size ** 2

