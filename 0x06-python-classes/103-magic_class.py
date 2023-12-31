#!/usr/bin/python3
import math

class MagicClass:
    """
    This is the MagicClass.
    """

    def __init__(self, radius=0):
        """
        This is the constructor method.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        This method calculates the area.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        This method calculates the circumference.
        """
        return 2 * math.pi * self.__radius

