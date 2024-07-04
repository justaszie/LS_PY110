"""
PROBLEM
- Input: list of numbers
- Output: list with the number of numbers that are lower than the corresponding number in input lists
- Rules:
    - the numbers that are smaller than given number should be only counted once (number of unique numbers)
    - If the input list only has one element, the output list will be 0
    -
- Questions
    -

ALGORITHM:
1. Create an empty result list
2. Iterate over each index. For each index i:
    A. create an empty set of lower numbers
    B. iterate over each index j except the current index. on each iteration:
        - Compare the number at the current index i to the number at the index j.
            - If the number at index j < number at index i:
                - add the number at index j to a set of lower numbers
    C. Append the length of the lower numbers set to the result list


"""

def smaller_numbers_than_current(lst):
    result = []
    for i in range(len(lst)):
        lower_numbers = { lst[j] for j in range(len(lst)) if j != i and lst[j] < lst[i] }
        result.append(len(lower_numbers))

    return result


print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)
