#!/usr/bin/python3
import json
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
        Constructor for the Base class.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

