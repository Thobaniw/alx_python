"""
This module contains the Square class that inherits from Rectangle.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square, inheriting from the Rectangle class.

    Attributes:
        size (int): Size of the square.
        x (int): X-coordinate position of the square.
        y (int): Y-coordinate position of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): Size of the square.
            x (int, optional): X-coordinate position of the square. Defaults to 0.
            y (int, optional): Y-coordinate position of the square. Defaults to 0.
            id (int, optional): Unique identifier of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """int: The size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a formatted string representation of the square.

        Returns:
            str: A formatted string representing the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
