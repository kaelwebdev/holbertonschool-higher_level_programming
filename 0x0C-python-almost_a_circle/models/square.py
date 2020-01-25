#!/usr/bin/python3
"""
this is module square.
this modole has the following classes:
Square.
"""

from models.rectangle import Rectangle

def int_check(n, v):
    """check if is a valid integer."""
    w = ['size', 'x', 'y']
    if type(v) != int:
        raise TypeError("{} must be an integer".format(n))
    if n == w[0] and v <= 0:
        raise ValueError("{} must be > 0".format(n))
    if (n == w[1] or n == w[2]) and v < 0:
        raise ValueError("{} must be >= 0".format(n))



class Square(Rectangle):
    """The class Saquare."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize attributes."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Instance method that returns an “informal”
        and nicely printable string representation
        of an instance.
        """
        return ('[Square] ({}) {}/{} - {}'.format(self.id,
                self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """
        Overwrite multiple attribute values.
        indeterminate arguments by position
        and name are used.
        """
        if args:
            l = ['id', 'size', 'x', 'y']
            for idx, v in enumerate(args):
                setattr(self, l[idx], v)
            return
        for k in kwargs:
            if hasattr(self, k):
                setattr(self, k, kwargs[k])

    @property
    def size(self):
        """get size."""
        return self.width

    @size.setter
    def size(self, value):
        """set size""" 
        int_check('size', value)
        self.width = value
        self.height = value
