'''
Integer validator
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
