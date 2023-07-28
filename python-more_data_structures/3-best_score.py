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


# Test cases
# Example 1
a_dictionary1 = {'John': 90, 'Alice': 85, 'Bob': 95, 'Eva': 88}
print(best_score(a_dictionary1))  # Output: 'Bob'

# Example 2
a_dictionary2 = {'Math': 75, 'History': 92, 'English': 83}
print(best_score(a_dictionary2))  # Output: 'History'

# Example 3 (Empty dictionary)
a_dictionary3 = {}
print(best_score(a_dictionary3))  # Output: None
