"""
PROBLEM
- Input: Positive integer 
- Output: List of integers between 1 and the input, inclusive
- Explicit Rules: List of integers between 1 and the input, inclusive
- Implicit Rules:
    - Assumption: Positive integer here means greater than 0
- Question:
    - Positive integer here means greater than 0?

EXAMPLES
print(sequence(5))    # [1, 2, 3, 4, 5]
print(sequence(3))    # [1, 2, 3]
print(sequence(1))    # [1]

DATA STRUCTURES
Integers, Lists. Potentially, ranges

ALGORITHM
1. Create a list of integers starting from one, up to the input integer value, inclusive
2. Return the list
"""

def sequence(number):
    return list(range(1,number + 1))


print(sequence(5))    # [1, 2, 3, 4, 5]
print(sequence(3))    # [1, 2, 3]
print(sequence(1))    # [1]