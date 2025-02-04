#!/usr/bin/python3

"""
Module for custom list (inherits from list)
"""


class MyList(list):
    """Custom list with sorted print and no infinity values."""
    
    def print_sorted(self):
        """Prints the list sorted, excluding infinity values."""
        print(sorted(x for x in self if x not in [float('inf'), float('-inf')]))

    def append(self, item):
        """Appends item, raises error if it's infinity."""
        if item in [float('inf'), float('-inf')]:
            raise ValueError("Cannot append infinity values.")
        super().append(item)
