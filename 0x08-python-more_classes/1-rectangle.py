#!/usr/bin/python3
"""this defines the rectangle"""
class Rectangle:
    """
    A class to represent a rectangle.

    ...

    Attributes
    ----------
    width : int
        width of the rectangle (default is 0)
    height : int
        height of the rectangle (default is 0)

    Methods
    -------
    None for now.
    """

    def __init__(self, width=0, height=0):
        """
        Constructs all the necessary attributes for the rectangle object.

        Parameters
        ----------
            width : int
                width of the rectangle (default is 0)
            height : int
                height of the rectangle (default is 0)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """int: Gets or sets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Parameters
        ----------
            value : int
                width of the rectangle

        Raises
        ------
        TypeError
            If width is not an integer.
        ValueError
            If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """int: Gets or sets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Parameters
        ----------
            value : int
                height of the rectangle

        Raises
        ------
        TypeError
            If height is not an integer.
        ValueError
            If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

