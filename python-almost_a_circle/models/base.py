"""
This module contains the base class for managing id attributes in all other classes.

Classes:
    Base: The base class with methods to manage id attributes.
"""


class Base:
    """
    The base class for managing id attributes in all other classes.

    Attributes:
        __nb_objects (int): A private class attribute to keep track of the number of objects created.

    Methods:
        __init__(self, id=None): Class constructor to initialize id attribute.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize an instance of the Base class.

        Args:
            id (int, optional): An integer representing the id of the instance. If provided, assigns this value to the id attribute. If not provided, increments __nb_objects and assigns the new value to the id attribute.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
