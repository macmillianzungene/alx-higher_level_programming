#!/usr/bin/python3
"""
This module contains the Rectangle class that inherits from Base.
"""

from models.base import Base

class Rectangle(Base):
    """
    This is the Rectangle class that inherits from Base.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        This is the constructor of the Rectangle class.

        Args:
            width (int): The width of the Rectangle instance.
            height (int): The height of the Rectangle instance.
            x (int, optional): The x of the Rectangle instance. Defaults to 0.
            y (int, optional): The y of the Rectangle instance. Defaults to 0.
            id (int, optional): The id of the Rectangle instance. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

