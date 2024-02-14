#!/usr/bin/python3

"""rectangle class defined here"""


class Rectangle:
    """this be a rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        string = ''
        if self.height == 0 or self.width == 0:
            return string
        for i in range(0, self.height):
            string += '#' * self.width
            if i < self.height - 1:
                string += '\n'
        return string

    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        print('Bye rectangle...')

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if (self.width == 0 or self.height == 0):
            return 0
        return 2 * (self.height + self.width)
