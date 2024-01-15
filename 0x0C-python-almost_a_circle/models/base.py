#!/usr/bin/python3
"""
This module contains the Base class.
"""

class Base:
    """
    This is the Base class.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        This is the constructor of the Base class.

        Args:
            id (int, optional): The id of the Base instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

