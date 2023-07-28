def update_dictionary(a_dictionary, key, value):
    new_dict = dict(a_dictionary)  # copy of the original dictionary
    new_dict[key] = value
    return new_dict


# Test cases
a_dictionary = {'a': "a", 'b': "b", 'c': "c", 'd': "d", 'e': "e"}
print(update_dictionary(a_dictionary, "a", "A"))
print(update_dictionary(a_dictionary, "e", "E"))
print(update_dictionary(a_dictionary, "a", 89))
print(update_dictionary(a_dictionary, "e", [1, 2, 3]))
print(update_dictionary(a_dictionary, "f", "A"))
print(update_dictionary({}, "a", "a"))
