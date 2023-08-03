'''
Access and update private attributes
'''


class Square:
    """
    This class defines a square.

    Private instance attribute:
    __size (int): The size of the square.

    Instantiation with optional size, which must be an integer >= 0.

    Public instance method:
    area(self): Returns the current square area.
    """

    def __init__(self, size=0):
        """
        Initializes a new square with the given size.

        Parameters:
        size (int, optional): The size of the square. Defaults to 0.
        """
        self.__size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square.

        Returns:
        int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the square.

        Parameters:
        value (int): The new size to set for the square.

        Raises:
        TypeError: If the value is not an integer.
        ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
        int: The area of the square.
        """
        return self.__size * self.__size
