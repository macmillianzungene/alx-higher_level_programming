#!/usr/bin/python3
from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the Square.

        Args:
            value (int): The new size of the Square.
        """
        self.width = self.height = value

    def __str__(self):
        """Return an informal and nicely printable string of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)

