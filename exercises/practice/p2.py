"""
PROBLEM
- Input: list of integers
- Output: minimum sum of 5 consecutive numbers. None if len < 5
- Rules:
    - Create a list of sums of 5 consecutive numbers
    - Return the minimum
    - Assuming only integers




ALGORITHM
1. If lenght of the list is < 5, return None
[*] 1. Create a sequence of sums of 5 consec numbers
2. Return the minimum of the sequence


* Calculating sums
1. Create an empty sums list
2. Iterate over indices from 0 to len(lst) - 5 (incl). On each iteration:
    A. Calculate the sum of part of lst from current index to len(lst)
    B. Append the calcualted sum to sums list

Indices:
5 elem: 0-4
    - 0-4
6 elem: 0-5:
    - 0-4
    - 1-5
"""

def minimum_sum(lst):
    if len(lst) < 5:
        return None

    sums = []

    for idx in range(len(lst) - 4):
        sum_5 = sum(lst[idx:idx + 5])
        sums.append(sum_5)

    return min(sums)

print(minimum_sum([10,2,3, 50, 5,6]))
print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)
