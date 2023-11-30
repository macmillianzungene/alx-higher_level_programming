#!/usr/bin/python3
import sys

def sum_args():
    args = map(int, sys.argv[1:])
    print(sum(args))

if __name__ == "__main__":
    sum_args()

