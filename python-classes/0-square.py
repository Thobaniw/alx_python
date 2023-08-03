'''
Square with size
'''


class Square:
    """
    This class defines a square.

    Private instance attribute:
    __size (int): The size of the square.

    Instantiation with size (no type/value verification).
    """

    def __init__(self, size):
        """
        Initializes a new square with the given size.

        Parameters:
        size (int): The size of the square.
        """
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
