"""
PROBLEM
Input: MxN Matrix (nested lists)
Output: Rotated matrix as a new object
Rules:
    - The output is a new object - don't mutate the input
    - The output is the input matrix (nested lists), rotated by 90 degrees (see examples)
    - Assuming that the matrix is at least 1 row and 1 column (in which case the output would be the same)
    - N and M may not be equal

Result is transposed but nested lists are in reverse order.

ALGORITHM
1. Transpose the matrix
    - Create a list of of len(input_matrix) length. Create sublists for each row of this list
    - Go over each row of original matrix. Append the elements to the sublists at i-th position
2. Go over each nested list and reverse its order


"""

def transpose(matrix):
    transposed = [ [] for _ in range(len(matrix[0])) ]

    for row in matrix:
        for idx, element in enumerate(row):
            transposed[idx].append(element)

    return transposed


def rotate90(matrix):
    transposed_matrix = transpose(matrix)
    for row in transposed_matrix:
        row.reverse()

    return transposed_matrix

matrix1 = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

#  Expected:
#  [
# [3, 4, 1],
# [9, 7, 5],
# [6, 2, 8]
# ]

matrix2 = [
    [3, 7, 4, 2],
    [5, 1, 0, 8],
]


new_matrix1 = rotate90(matrix1)
new_matrix2 = rotate90(matrix2)
new_matrix3 = rotate90(rotate90(rotate90(rotate90(matrix2))))

# These examples should all print True
print(new_matrix1 == [[3, 4, 1], [9, 7, 5], [6, 2, 8]])
print(new_matrix2 == [[5, 3], [1, 7], [0, 4], [8, 2]])
print(new_matrix3 == matrix2)

