#!/usr/bin/python3
"""
This module contains a unittest for the function max_integer in the module my_module.

The function max_integer takes a list as input and returns the maximum integer in the list.
"""

import unittest
import my_module

class TestMaxInteger(unittest.TestCase):
    """
    Defines a class to test the function max_integer.
    """

    def test_max_integer(self):
        """
        Tests the function max_integer with various inputs.

        Args:
            self: The instance of the class.

        Returns:
            None
        """
        self.assertEqual(my_module.max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(my_module.max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(my_module.max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(my_module.max_integer([1]), 1)
        self.assertEqual(my_module.max_integer([]), None)
        self.assertRaises(TypeError, my_module.max_integer, [1, "2", 3, 4])

if __name__ == '__main__':
    unittest.main()

