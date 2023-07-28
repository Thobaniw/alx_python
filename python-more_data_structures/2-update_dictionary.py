def update_dictionary(a_dictionary, key, value):
    """Replaces or adds key/value in a dictionary.

    Args:
        a_dictionary (dict): The dictionary to update.
        key (str): The key to update.
        value: The value to set for the key.

    Returns:
        None.
    """

    if key in a_dictionary:
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value


def main():
    a_dictionary = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e'}

    update_dictionary(a_dictionary, 'a', 'A')

    print('xx')

    for key, value in a_dictionary.items():
        print(f'{key}: {value}')


if __name__ == '__main__':
    main()
