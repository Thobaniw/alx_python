
def raise_exception_msg(message=""):
    raise NameError(message)

try:
    raise_exception_msg("This is a name exception.")
except NameError as ne:
    print("Exception raised:", ne)

print("C is fun")