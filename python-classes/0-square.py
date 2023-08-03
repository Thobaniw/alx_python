class Square:
    def __init__(self, size):
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def perimeter(self):
        return 4 * self.__size
