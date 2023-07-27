def square_matrix_simple(matrix):
    """Computes the square value of all integers of a matrix.

    Args:
      matrix: A 2 dimensional array.

    Returns:
      A new matrix:
        Same size as matrix
        Each value should be the square of the value of the input
      Initial matrix should not be modified

    """

    new_matrix = []
    for row in matrix:
        new_row = []
        for value in row:
            new_value = value ** 2
            new_row.append(new_value)
        new_matrix.append(new_row)
    return new_matrix


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    new_matrix = square_matrix_simple(matrix)
    print(new_matrix)
