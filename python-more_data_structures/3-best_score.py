def best_score(a_dictionary):
    if not a_dictionary or not isinstance(a_dictionary, dict):
        return None

    # Check if all values are integers
    if not all(isinstance(value, int) for value in a_dictionary.values()):
        return None

    # Find the key with the maximum value (score)
    max_key = max(a_dictionary, key=a_dictionary.get)

    return max_key
