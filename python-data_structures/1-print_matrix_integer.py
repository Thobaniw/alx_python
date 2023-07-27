def print_matrix_integer(matrix=[[]]):
    # The number of rows and columns in the matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if matrix else 0

    #  The maximum width of each cell to format the output
    max_width = max(len(str(matrix[i][j])) for i in range(num_rows) for j in range(num_cols))

    # To print the matrix
    for i in range(num_rows):
        for j in range(num_cols):
            # Format each element and align them to the right
            cell = "{:>{width}}".format(matrix[i][j], width=max_width)
            #  To  print the cell without a newline to keep elements in the same row
            print(cell, end=" ")
        print()


