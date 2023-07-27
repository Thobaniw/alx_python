def print_matrix_integer(matrix=[[]]):
    # Get the number of rows and columns in the matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if matrix else 0

    # Calculate the maximum width of each cell to format the output
    max_width = max(len("{:d}".format(matrix[i][j])) for i in range(num_rows) for j in range(num_cols))

    # Print the matrix
    for i in range(num_rows):
        for j in range(num_cols):
            # Format each element and align them to the right
            cell = "{:>{width}}".format(matrix[i][j], width=max_width)
            # Print the cell without a newline to keep elements in the same row
            print(cell, end=" ")
        # Move to the next row after printing all elements in the current row
        print()

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print_matrix_integer(matrix)





