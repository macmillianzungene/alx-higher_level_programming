#!/usr/bin/python3
def uppercase(str):
    result = ''
    for c in str:
        ascii_val = ord(c)
        if ascii_val >= 97 and ascii_val <= 122:
            result += chr(ascii_val - 32)
        else:
            result += c
    print(result)
