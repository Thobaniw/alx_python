def best_score(a_dictionary):
    # Check if the dictionary is empty
    if not a_dictionary:
        return None

    # Sort the dictionary items by values in descending order
    sorted_items = sorted(a_dictionary.items(),
                          key=lambda item: item[1], reverse=True)

    # Get the student with the highest score
    best_student = sorted_items[0][0]

    return best_student


# Test case
my_dict = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
best_student = best_score(my_dict)
print(f"Best: {best_student}")
