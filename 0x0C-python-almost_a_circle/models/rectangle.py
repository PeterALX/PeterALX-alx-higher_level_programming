#!/usr/bin/python3
"""class Rectangle"""

from models.base import Base


class Rectangle(Base):
    """Class that defines properties of Rectangle.
     Attributes:
        width (int): width of rectangle.
        height (int): height of rectangle.
        x (int): x.
        y (int): y.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super.__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width retriever.
        Returns:
            int: width of rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Property setter for width of rectangle.
        Args:
            value (int): width of rectangle.
        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less than or equal to zero.
        """
        self.__width = value
