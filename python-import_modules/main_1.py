def raise_exception_msg(message=""):
    raise NameError(message)

try:
    raise_exception_msg("Python is cool")
except NameError as ne:
    print("Exception raised:", ne)

print("Python is cool")
