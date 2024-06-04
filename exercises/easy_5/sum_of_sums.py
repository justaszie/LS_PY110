"""
PROBLEM
- Input: List of numbers 
- Output: Integer: sum of running totals
- Explicit Rules:
    - Input list will have at least 1 number
    - The output is the sum of running totals at each position. 
- Implicit Rules
    - Assuming numbers will be integers
    - At each position of input list, we need to calculate the running total and then calculate the sum of those running totals
- Questions: 
    - Assuming numbers will be integers

EXAMPLES
print(sum_of_sums([3, 5, 2]))        # (3) + (3 + 5) + (3 + 5 + 2) --> 21
print(sum_of_sums([1, 5, 7, 3]))     # (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36
print(sum_of_sums([4]))              # 4
print(sum_of_sums([1, 2, 3, 4, 5]))  # 35

DATA STRUCTURES
Lists and in tegers

ALGORITHM
1. Create an empty "totals" list
2. Calculate the running total at each position of the input list
    - Set current total to 0
    - Iterate over the input list. For each value:
        A. Add the value to the current total
        B. Add the current total to the "totals" list 
3. Calculate the sum of the running totals at each position
4. Return the sum

"""

def sum_of_sums(numbers):
    # V1
    # totals = []
    # current_total = 0

    # for number in numbers:
    #     current_total += number
    #     totals.append(current_total)

    # return sum(totals)

    # V2
    return sum([sum(numbers[:idx + 1]) for idx in range(len(numbers))])


print(sum_of_sums([3, 5, 2]))        # (3) + (3 + 5) + (3 + 5 + 2) --> 21
print(sum_of_sums([1, 5, 7, 3]))     # (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36
print(sum_of_sums([4]))              # 4
print(sum_of_sums([1, 2, 3, 4, 5]))  # 35

