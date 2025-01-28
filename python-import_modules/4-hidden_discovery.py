#!/usr/bin/python3
import sys
import os
import importlib.util

def discover_hidden_names():
    # Define the path to the hidden_4.pyc file
    file_path = "/tmp/hidden_4.pyc"

    # Load the .pyc file using importlib
    spec = importlib.util.spec_from_file_location("hidden_4", file_path)
    hidden_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_module)

    # Get all names defined in the module
    names = dir(hidden_module)

    # Filter and sort names that do not start with '__'
    valid_names = sorted(name for name in names if not name.startswith('__'))

    # Print each valid name
    for name in valid_names:
        print(name)

if __name__ == "__main__":
    discover_hidden_names()
