#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Print the first x integers of a list.

    Args:
    my_list (list): The list to print from. Can contain any type. Defaults to [].
    x (int): The number of elements to access in my_list. Defaults to 0.

    Returns:
    int: The actual number of integers printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, IndexError):
            continue
    print()
    return count

