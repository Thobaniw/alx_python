'''
 Square #1
'''


class BaseGeometry:
    """
    This class represents a base geometry.

    Public instance methods:
    - area(self): raises an Exception with the message "area() is not implemented"
    - integer_validator(self, name, value): validates the value as an integer.
    """

    def area(self):
        """
        Raise an Exception with the message "area() is not implemented".

        Raises:
        Exception: Always raises an exception with the specified message.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the value as an integer.

        Parameters:
        name (str): The name of the value to be validated.
        value (int): The value to be validated.

        Raises:
        TypeError: If the value is not an integer.
        ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    This class represents a rectangle, inheriting from BaseGeometry.

    Attributes:
    - __width (int): The width of the rectangle.
    - __height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize the Rectangle with width and height.

        Parameters:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
        str: The rectangle description in the format [Rectangle] <width>/<height>
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
        int: The area of the rectangle.
        """
        return self.__width * self.__height


class Square(Rectangle):
    """
    This class represents a square, inheriting from Rectangle.

    Attributes:
    - __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initialize the Square with size.

        Parameters:
        size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
        str: The square description in the format [Square] <size>/<size>
        """
        return f"[Square] {self.__width}/{self.__height}"

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
        int: The area of the square.
        """
        return self.__width * self.__height
