#!/usr/bin/python3

"""
Module that contains a function to check if an object is an instance
of a class.
"""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance of the class."""
    return type(obj) is a_class
