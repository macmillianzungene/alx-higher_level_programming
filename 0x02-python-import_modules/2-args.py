#!/usr/bin/python3
import sys

def main():
    num_args = len(sys.argv) - 1
    if num_args == 1:
        print("Number of argument: ", end="")
    else:
        print("Number of arguments: ", end="")

    if num_args == 0:
        print(".")
    else:
        print(f"{num_args}:")
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"{i}: {arg}")

if __name__ == "__main__":
    main()

