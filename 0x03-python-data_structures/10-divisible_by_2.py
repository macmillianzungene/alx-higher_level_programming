#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    This function takes a list of integers and returns a new list with True or False,
    depending on whether the integer at the same position in the original list is a multiple of 2.
    """
    return [i % 2 == 0 for i in my_list]

