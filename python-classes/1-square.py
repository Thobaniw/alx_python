'''
size validation
'''


class Square:
    """
    This class defines a square.

    Private instance attribute:
    __size (int): The size of the square.

    Instantiation with optional size, which must be an integer >= 0.
    """

    def __init__(self, size=0):
        """
        Initializes a new square with the given size.

        Parameters:
        size (int, optional): The size of the square. Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
        int: The area of the square.
        """
        return self.__size * self.__size

    def perimeter(self):
        """
        Calculates the perimeter of the square.

        Returns:
        int: The perimeter of the square.
        """
        return 4 * self.__size
