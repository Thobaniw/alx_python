def print_sorted_dictionary(my_dict):
    keys = sorted(my_dict.keys())
    for key in keys:
        print(f"{key}: {my_dict[key]}")


def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary


# Test case
a_dictionary = {'a': "a", 'b': "b", 'c': "c", 'd': "d", 'e': "e"}
new_dict = update_dictionary(a_dictionary.copy(), "a", "A")
print_sorted_dictionary(new_dict)
print("xx")
print_sorted_dictionary(a_dictionary.copy())
