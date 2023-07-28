def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary


# Examples
my_dict = {"name": "John", "age": 30}
print(update_dictionary(my_dict, "name", "Alice"))
print(update_dictionary(my_dict, "city", "New York"))
