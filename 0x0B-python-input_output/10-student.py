#!/usr/bin/python3
"""
This module defines a Student class.
"""


class Student:
    """
    Defines a Student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes the student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of strings to be retrieved. If it's None, all attributes will be retrieved.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if attr in self.__dict__}

