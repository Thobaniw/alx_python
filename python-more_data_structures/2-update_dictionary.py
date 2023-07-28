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


a_dictionary = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e'}

update_dictionary(a_dictionary, 'a', 'A')
update_dictionary(a_dictionary, 'f', 'F')

for key, value in a_dictionary.items():
    print(f'{key}: {value}')
