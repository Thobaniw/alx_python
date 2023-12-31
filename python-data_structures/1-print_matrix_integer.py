
def print_matrix_integer(matrix=[[]]):
    # Get the number of rows and columns in the matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if matrix else 0

    if num_rows == 0 or num_cols == 0:
        # Handle the case of an empty matrix
        print()
        return

    # Calculate the maximum width of each cell to format the output
    max_width = max(len("{:d}".format(matrix[i][j])) for i in range(num_rows) for j in range(num_cols))

    # Print the matrix
    for i in range(num_rows):
        for j in range(num_cols):
            # Format each element and align them to the right
            cell = "{:>{width}d}".format(matrix[i][j], width=max_width)
            # Print the cell without a newline to keep elements in the same row
            print(cell, end="")
            if j < num_cols - 1:
                # Print a space between elements in the same row
                print(" ", end="")
        print()

