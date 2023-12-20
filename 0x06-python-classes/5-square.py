#!/usr/bin/python3
"""
This module defines a Square class
"""


class Square:
    """
    A class that defines a square by:
    - Private instance attribute: size
    - Instantiation with optional size: def __init__(self, size=0)
    - Public instance method: def area(self)
    - Public instance method: def my_print(self)
    """

    def __init__(self, size=0):
        """
        Initialize the Square instance

        Parameters:
        - size (int): size of the square
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieve the size of the Square instance
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the Square instance

        Parameters:
        - value (int): size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculate the area of the Square instance
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the Square instance with the character #
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

