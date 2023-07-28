def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    for k, v in a_dictionary.items():
        print(f"{k}: {v}")
    print("xx")
    return a_dictionary


# Test cases
a_dictionary = {'a': "a", 'b': "b", 'c': "c", 'd': "d", 'e': "e"}
# update_dictionary(a_dictionary.copy(), "a", "A")
# update_dictionary(a_dictionary.copy(), "e", "E")
# update_dictionary(a_dictionary.copy(), "a", 89)
# update_dictionary(a_dictionary.copy(), "e", [1, 2, 3])
# update_dictionary(a_dictionary.copy(), "f", "A")
u  # pdate_dictionary({}, "a", "a")
