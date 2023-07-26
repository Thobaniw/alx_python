def raise_exception_msg(msg):
    raise NameError(msg)

try:
    # Test case 3: message = ""
    raise_exception_msg("")
except NameError as ne:
    print(ne)

