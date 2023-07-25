
raise_exception = __import__('4-raise_exception').raise_exception_msg
try:
    raise_exception()
except Exception as e:
    print("Exception has been raised")

