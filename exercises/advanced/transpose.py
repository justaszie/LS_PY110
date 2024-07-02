"""
PROBLEM
- Input: a list of lists (matrix of rows and columns )
- Output: transposed matrix - columns to rows and rows to columns
- Rules:
    - The original matrix should not be modified. Function should return a new one.

ALGORITHM
1. Create a result list that contains N empty lists, where N is the length of the 1st row of input list
2. Iterate over the rows of the input list, keeping track of row index R. For each row:
    A. Iterate over each element of the row, keeping track the index of the element E. For each element:
        Append the element to the Xth sublist inside the result list. X here = E

R
E


1589
4723

14
57
82
93

Iter 1
    1; 5; 8  => [ [1], [5], [8] ]


"""
def transpose(matrix):
    result = [ [] for _ in matrix[0] ]
    for row in matrix:
        for idx, element in enumerate(row):
            result[idx].append(element)

    return result


matrix_3_by_5 = [
    [1, 2, 3, 4, 5],
    [4, 3, 2, 1, 0],
    [3, 7, 8, 6, 2],
]
expected_result = [
    [1, 4, 3],
    [2, 3, 7],
    [3, 2, 8],
    [4, 1, 6],
    [5, 0, 2],
]

print(transpose(matrix_3_by_5) == expected_result)

# matrix = [
#     [1, 5, 8],
#     [4, 7, 2],
#     [3, 9, 6],
# ]

# new_matrix = transpose(matrix)

# print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
# print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True