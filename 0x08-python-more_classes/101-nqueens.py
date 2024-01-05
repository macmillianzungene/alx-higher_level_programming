#!/usr/bin/python3
"""imported sys"""

import sys

def solveNQueens(n):
    def can_place(pos, ocuppied_positions):
        for i in range(len(ocuppied_positions)):
            if ocuppied_positions[i] == pos or \
                ocuppied_positions[i] - i == pos - len(ocuppied_positions) or \
                ocuppied_positions[i] + i == pos + len(ocuppied_positions):
                return False
        return True

    def place_queen(n, index, ocuppied_positions):
        if index == n:
            return [ocuppied_positions]
        else:
            results = []
            for pos in range(n):
                if can_place(pos, ocuppied_positions):
                    results += place_queen(n, index + 1, ocuppied_positions + [pos])
            return results

    return place_queen(n, 0, [])

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)

results = solveNQueens(n)
for result in results:
    print([[i, result[i]] for i in range(n)])

