"""
PROBLEM
- Input: List of integers
- Output: Tuple of 2 numbers that are closest together in value
- Rules:
    - If multiple pairs are equally close, return the 1st occuring pair.
- Questions:
    - What to return if the list is empty or has < 2 elements

ALGORITHM
1. Collect all pairs of numbers
2. Find and return the pair that has the smallest difference.


1 - detail
    0. Create empty list for pairs
    1. Iterate over the indexes of the list I from 0 to len(list) - 1 (excluded). On each iteration:
        A. Iterate over the indexes to the right of I and to the end of the list - J. On each iteration:
            append the pair of elements at indexes I and J to the list of pairs

[0] [1] [2]
5   6   8

Iteration 0
    0, 1 | 0, 2
Iteration 1
    1, 2

[i:j+1]

2 - detail
    1. Assign the difference of the 1st pair to a current minimum variable
    2. Assign the first pair as minimum pair
    2. Iterate over remaining pairs. On each iteration:
        A. If the difference between the pair is < than current minimum variable:
            - Reassign current minimum variable to the difference of the pair
            - Reassign current minimum pair variable to the current pair


"""
def get_pairs(lst):
    pairs = []
    for start in range(len(lst) - 1):
        for end in range(start + 1, len(lst)):
            pairs.append((lst[start], lst[end]))
    return pairs


def closest_numbers(lst):
    if not lst or len(lst) < 2:
        return None

    pairs = get_pairs(lst)

    min_pair = pairs[0]
    min_diff = abs(pairs[0][0]- pairs[0][1])

    for pair in pairs[1:]:
        current_diff = abs(pair[0] - pair[1])
        if current_diff < min_diff:
            min_pair = pair
            min_diff = current_diff

    return min_pair


print(closest_numbers([5, 25, 15, 11, 20]))
print(closest_numbers([19, 25, 32, 4, 27, 16]))
print(closest_numbers([12, 22, 7, 17]))

# print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
# print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
# print(closest_numbers([12, 22, 7, 17]) == (12, 7))