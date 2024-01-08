#!/usr/bin/python3
"""
This module contains a class MyList that inherits from list.
"""


class MyList(list):
    """
    MyList class. This class inherits from list and includes a method to print
    the list sorted in ascending order.
    """

    def print_sorted(self):
        """
        Public instance method that prints the list sorted in ascending order.
        Assumes that all elements of the list are of type int.
        """
        print(sorted(self))

