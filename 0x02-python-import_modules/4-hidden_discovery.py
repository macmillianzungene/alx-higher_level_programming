#!/usr/bin/python3
import importlib

def print_names():
    module = importlib.import_module('hidden_4')
    names = sorted(name for name in dir(module) if not name.startswith('__'))
    print('\n'.join(names))

if __name__ == "__main__":
    print_names()

