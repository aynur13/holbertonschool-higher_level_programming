#!/usr/bin/python3
import sys
import importlib.util

if __name__ == "__main__":

    module_path = '/tmp/hidden_4.pyc'
    
    spec = importlib.util.spec_from_file_location("hidden_4", module_path)
    hidden_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_module)
    
    names = [name for name in dir(hidden_module) if not name.startswith('__')]

    for name in sorted(names):
        print(name)

