#!/usr/bin/python3
"""
This module defines a Square class
"""


class Square:
    """
    A class that defines a square by:
    - Private instance attribute: size
    - Instantiation with size: def __init__(self, size=0)
    - Public instance method: def area(self)
    """

    def __init__(self, size=0):
        """
        Initialize the Square instance

        Parameters:
        - size (float or int): size of the square
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
        - value (float or int): size of the square
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculate the area of the Square instance
        """
        return self.__size ** 2

    def __eq__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() == other.area()

    def __ne__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() != other.area()

    def __lt__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() < other.area()

    def __le__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() <= other.area()

    def __gt__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() > other.area()

    def __ge__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() >= other.area()

