def common_elements(set_1, set_2):
    """Returns a set of common elements in two sets.

    Args:
      set_1: A set.
      set_2: A set.

    Returns:
      A set of common elements in two sets.

    """

    common_elements = set()
    for element in set_1:
        if element in set_2:
            common_elements.add(element)
    return common_elements


if __name__ == "__main__":
    set_1 = {1, 2, 3, 4, 5}
    set_2 = {2, 3, 5, 6, 7}
    common_elements = common_elements(set_1, set_2)
    print(common_elements)
