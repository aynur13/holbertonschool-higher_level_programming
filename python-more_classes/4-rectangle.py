#!/usr/bin/python3
""" Rectangle Module, For rectangular purposes only. """


class Rectangle:
    """ Rectangle class """
    def __init__(self, width=0, height=0):
        """ init """
        self.width = width
        self.height = height

    def __str__(self):
        """ string conversion """
        # this will print area width * height
        string = (('#' * self.__width) + '\n') * self.__height
        return string[:-1]
    # repr() should return a string representation
    # of the rectangle to be able to recreate a
    # new instance by using eval()

    def __repr__(self):
        """ string conversion """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """ returns area of rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ returns perimeter of rectangle """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
