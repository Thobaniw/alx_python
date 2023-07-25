def import_raise_exception():
  """Imports the raise_exception module."""

  raise_exception = __import__('4-raise_exception')
  return raise_exception.raise_exception


def main():
  """Raises an exception."""

  raise_exception = import_raise_exception()
  raise_exception()


if __name__ == "__main__":
  main()
