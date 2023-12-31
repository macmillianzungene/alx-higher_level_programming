#!/usr/bin/python3
"""
This module imports functions from calculator_1.py, performs some calculations, and prints the results.
"""

from calculator_1 import add, sub, mul, div


def main():
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))

if __name__ == "__main__":
    main()

