#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""
    
    def __init__(self, size=0):
        """Initialize a new square with size validation."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
           def get_size(self)
           raise ValueError("size must be >= 0")
        return self._size = size
