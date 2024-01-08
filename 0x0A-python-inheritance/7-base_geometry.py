#!/usr/bin/python3
"""
This module contains a class BaseGeometry with two public instance methods:
'area' and 'integer_validator'.
"""


class BaseGeometry:
    """
    This is a class named BaseGeometry with two public instance methods:
    'area' and 'integer_validator'.
    """

    def area(self):
        """
        This method raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This method validates 'value'.

        Args:
            name: A string.
            value: An integer.

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is less or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

