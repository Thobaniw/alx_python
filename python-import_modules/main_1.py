def raise_exception_msg(msg):
    if not msg:
        raise NameError
    raise NameError(msg)

try:
    # Test case 2: message = "Python is cool"
    raise_exception_msg("Python is cool")
except NameError as ne:
    print(ne)
