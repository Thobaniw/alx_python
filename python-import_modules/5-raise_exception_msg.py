def raise_exception_msg(message=""):
    raise NameError(message)

# to Test the function
try:
    raise_exception_msg("This is a name exception.")
except NameError as ne:
    print("Exception raised:", ne)
