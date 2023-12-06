#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Function to add all unique integers in a list.

    Args:
    my_list (list): The initial list of integers.

    Returns:
    sum (int): Sum of all unique integers in the list.
    """
    # Create a set from the list to remove duplicates
    unique_set = set(my_list)

    # Return the sum of the unique integers
    return sum(unique_set)

