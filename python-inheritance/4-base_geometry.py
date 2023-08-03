'''
Improve Geometry
'''


class BaseGeometry:
    """
    This class represents a base geometry.

    Public instance method:
    - area(self): raises an Exception with the message "area() is not implemented"
    """

    def area(self):
        """
        Raise an Exception with the message "area() is not implemented".

        Raises:
        Exception: Always raises an exception with the specified message.
        """
        raise Exception("area() is not implemented")
