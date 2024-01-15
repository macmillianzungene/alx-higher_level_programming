#!/usr/bin/python3
from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = self.height = value

    def __str__(self):
        """Return the print() and str() representation."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

