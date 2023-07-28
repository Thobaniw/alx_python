def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    for k, v in a_dictionary.items():
        print(f"{k}: {v}")
    print("xx")
    return a_dictionary


# Test cases
a_dictionary = {'a': "a", 'b': "b", 'c': "c", 'd': "d", 'e': "e"}
print(update_dictionary(a_dictionary, "a", "A"))
print(update_dictionary(a_dictionary, "e", "E"))
print(update_dictionary(a_dictionary, "a", 89))
print(update_dictionary(a_dictionary, "e", [1, 2, 3]))
print(update_dictionary(a_dictionary, "f", "A"))
print(update_dictionary({}, "a", "a"))
