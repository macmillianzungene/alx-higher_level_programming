#!/usr/bin/python3
"""
This module defines a class Square that inherits from Rectangle.
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

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the rectangle description.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """
    def __init__(self, size):
        """
        Initializes a new instance of Square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns the square description.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)

