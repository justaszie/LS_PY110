"""
PROBLEM
- Input: list of integers
- Output: Number of identical pairs of numbers
- Rules:
    - Identical pair = 2 same integers e.g. (2, 2)
    - The pair must be complete (e.g. in [7, 7, 7] there is only 1 complete pair)
    - If the list is empty or has 1 element, return 0
    -
- Questions:
    - List such as [1, 2] returns 1?

7, 7, 7

ALGORITHM
1. Count occurences of each unique number.
2. Keep only the numbers that have a pair amount of occurences
3. Return the lenght of the remaining list of numbers

1 - counting
    1. Create a set from the list
    2. Iterate over the set and store the count of occurences in the input list (dict with number:occurences)

2 - create a list with the numbers that have pair number of occurences

3-  return the lenght of the list

"""

def pairs(lst):
    if not lst or len(lst) == 1:
        return 0

    occurences = {}
    for number in lst:
        occurences[number] = occurences.get(number, 0) + 1

    # unique_numbers = set(lst)



    # for number in unique_numbers:
    #     occurences[number] = lst.count(number)

    # # print(occurences)

    identical_pairs = 0

    for key, value in occurences.items():
        identical_pairs += value // 2

    return identical_pairs


print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
print(pairs([]) == 0)
print(pairs([23]) == 0)
print(pairs([997, 997]) == 1)
print(pairs([32, 32, 32]) == 1)
print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)
