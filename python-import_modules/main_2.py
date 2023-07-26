def raise_exception_msg(msg):
    if not msg:
        raise NameError
    raise NameError(msg)

try:
    # Test case 3: message = ""
    raise_exception_msg("")
except NameError as ne:
    print(ne)
