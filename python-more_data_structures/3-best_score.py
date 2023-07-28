def best_score(a_dictionary):
    # Check if the dictionary is empty
    if not a_dictionary:
        return None

    max_value = None
    max_key = None

    # Iterate through the dictionary to find the key with the biggest integer value
    for key, value in a_dictionary.items():
        if isinstance(value, int):
            if max_value is None or value > max_value:
                max_value = value
                max_key = key

    return max_key


# Test case
my_dict = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
best_student = best_score(my_dict)
print(f"Best: {best_student}")
