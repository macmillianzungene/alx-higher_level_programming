#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Function to replace all occurrences of an element by another in a new list.

    Args:
    my_list (list): The initial list.
    search: The element to replace in the list.
    replace: The new element.

    Returns:
    new_list (list): List with all occurrences of 'search' replaced by 'replace'.
    """
    # Create a new list
    new_list = []

    # Iterate over each element in the list
    for element in my_list:
        # If the element is the one we are searching for, replace it
        if element == search:
            new_list.append(replace)
        # Otherwise, keep the original element
        else:
            new_list.append(element)

    # Return the new list
    return new_list

