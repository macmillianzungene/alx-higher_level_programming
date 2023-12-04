#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    This function deletes the item at a specific position in a list.
    If idx is negative or out of range, it returns the same list.
    """
    if 0 <= idx < len(my_list):
        my_list = my_list[:idx] + my_list[idx+1:]
    return my_list

