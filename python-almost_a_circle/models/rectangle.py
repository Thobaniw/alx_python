"""
This module contains the Rectangle class that inherits from Base.
"""

from models.base import Base


class Rectangle(Base):
    """
    Represents a rectangle, inheriting from the Base class.

    Attributes:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        x (int): X-coordinate position of the rectangle.
        y (int): Y-coordinate position of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): X-coordinate position of the rectangle. Defaults to 0.
            y (int, optional): Y-coordinate position of the rectangle. Defaults to 0.
            id (int, optional): Unique identifier of the rectangle. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle."""
        self.__height = value

    @property
    def x(self):
        """int: The X-coordinate position of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the X-coordinate position of the rectangle."""
        self.__x = value

    @property
    def y(self):
        """int: The Y-coordinate position of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the Y-coordinate position of the rectangle."""
        self.__y = value
