'''
 Only sub class of
'''


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited (directly or indirectly)
    from the specified class.

    Parameters:
    obj (any): The object to check.
    a_class (type): The specified class.

    Returns:
    bool: True if obj is an instance of a subclass of a_class; False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
