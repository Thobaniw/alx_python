def raise_exception_msg(msg):
    if not msg:
        raise NameError
    raise NameError(msg)

try:
    # Test case 1: message = "C is fun"
    raise_exception_msg("C is fun")
except NameError as ne:
    print(ne)

