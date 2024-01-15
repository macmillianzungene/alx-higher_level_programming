#!/usr/bin/python3
from models.rectangle import Rectangle

class Square(Rectangle):
    """
    This is a Square class that inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter for size.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for size.
        """
        self.width = self.height = value

    def __str__(self):
        """
        Overloading the __str__ method to return [Square] (<id>) <x>/<y> - <size>
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """
        Method that assigns attributes.
        """
        attributes = ["id", "size", "x", "y"]
        if args and len(args) > 0:
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Method that returns the dictionary representation of a Square.
        """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}

