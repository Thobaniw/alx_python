'''
Exact same objects
'''


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of the specified class.

    Parameters:
    obj (any): The object to check.
    a_class (type): The specified class.

    Returns:
    bool: True if obj is exactly an instance of a_class; False otherwise.
    """
    return type(obj) is a_class
