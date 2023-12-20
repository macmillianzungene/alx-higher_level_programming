#!/usr/bin/python3
"""
This module defines a Square class
"""


class Square:
    """
    A class that defines a square by:
    - Private instance attribute: size
    - Private instance attribute: position
    - Instantiation with optional size and optional position: def __init__(self, size=0, position=(0, 0))
    - Public instance method: def area(self)
    - Public instance method: def my_print(self)
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the Square instance

        Parameters:
        - size (int): size of the square
        - position (tuple): position of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Retrieve the position of the Square instance
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the Square instance

        Parameters:
        - value (tuple): position of the square
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
            print("\n" * self.__position[1], end="")
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

