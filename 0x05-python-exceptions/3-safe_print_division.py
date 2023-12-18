#!/usr/bin/python3
def safe_print_division(a, b):
    """Divide 2 integers and print the result.

    Args:
    a (int): The dividend.
    b (int): The divisor.

    Returns:
    float: The result of the division, otherwise: None.
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(result))
        return result

