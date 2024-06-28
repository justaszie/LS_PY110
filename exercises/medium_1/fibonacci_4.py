"""
Write a function that calculates and returns the index of the first Fibonacci number that has the number of digits specified by the argument. The first Fibonacci number has an index of 1. You may assume that the argument is always an integer greater than or equal to 2.

PROBLEM
- Input: int representing number of digits
- Output: int representing the index of the 1st Fib number that has the number of digits
- Explicit rules:
    - Calculate the sequence until the number with specified number of digits is reached. Return the index
- Implicit rules:
    - Indices start at 1
    - Assuming the argument will always be > 0

ALGORITHM
1. Start with procedural
2. Try recursion later


Procedural:
1. Create initial sequence with [1,1]
2. If argument is < 2, return 1
2. Iterate over integer numbers representing indices until stop, starting from 3rd number. Each iteration
    A. Calculate the number in sequence (n-2 + n-1)
    B. convert number to string.
    C. If the length of the string == input argument:
        return the current index number


IMPLEM NOTES:
A) While True with return when condition reached
B) While index < input
"""

import sys

def find_fibonacci_index_by_length(digits):
    if digits < 2:
        return 1

    sequence = [1, 1]
    index = 2
    number = 1

    while len(str(number)) < digits:
        number = sequence[index - 2] + sequence[index - 1]
        sequence.append(number)
        index += 1

    return index


sys.set_int_max_str_digits(50_000)

# All of these examples should print True
# The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)

# Next example might take a little while on older systems
print(find_fibonacci_index_by_length(10000) == 47847)