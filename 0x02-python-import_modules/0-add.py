#!/usr/bin/python3
"""
This module imports the function add from add_0.py and prints the result of the addition 1 + 2 = 3.
"""

from add_0 import add

def main():
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))

if __name__ == "__main__":
    main()
