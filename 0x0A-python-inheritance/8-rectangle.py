#!/usr/bin/python3
"""
This module defines a class Rectangle that inherits from BaseGeometry.
"""

class BaseGeometry:
    """
    BaseGeometry class for validating values.
    """
    def integer_validator(self, name, value):
        """
        Validates that 'value' is a positive integer.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Initializes a new instance of Rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

