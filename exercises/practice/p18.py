"""
PROBLEM
- Input: a list of integers
- Output: integer - index N
- Rules:
    - Output: sum of the numbers with index < N (0 to N-1) == sum of numbers at indexes (N+1 to len-1).
        - I.e. sum of numbers to the left = sum of numbers to the right
    - if index = 0, sum left = 0
    - if index = len(list) - 1, sum right = 0
    - If there is no satisfying index N, return -1
    - If multiple N indexes satisfy the conditions, return the smallest


- Questions:


ALGORITHM
- Iterate over all possible indexes of the list 0 to len(list) - 1 (incl.). On each iteration:
    - Calculate sum of the numbers to the left
        - if index == 0, sum left = 0
        - else: sum(numbers[0:index])

    - Calculate sum of the numbers to the right
        - if index == len(list) - 1, sum right = 0
        - else: sum(numbers[index + 1: len(list)])

    - if sum_left == sum_right:
        return the index
- Return -1 since no appropriate index was found


"""

def equal_sum_index(numbers_list):
    for index in range(0, len(numbers_list)):
        sum_left = 0 if index == 0 else sum(numbers_list[0:index])
        sum_right = 0 if index == len(numbers_list) - 1 else sum(numbers_list[index + 1: len(numbers_list)])
        if sum_left == sum_right:
            return index

print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)

# The following test case could return 0 or 3. Since we're
# supposed to return the smallest correct index, the correct
# return value is 0.
print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)