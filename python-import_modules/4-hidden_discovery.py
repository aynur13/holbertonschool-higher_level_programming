#!/usr/bin/python3
import sys
import importlib.util

if __name__ == "__main__":
    # Load the hidden_4.pyc module
    module_name = "hidden_4"
    module_path = "/tmp/hidden_4.pyc"
    
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    hidden_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_module)
    
    # Get all the names defined in the module, filter out those starting with '__'
    names = [name for name in dir(hidden_module) if not name.startswith('__')]
    
    # Sort and print the names
    for name in sorted(names):
        print(name)
