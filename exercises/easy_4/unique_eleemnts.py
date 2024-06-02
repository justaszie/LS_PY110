"""
PROBLEM 
- Input: 2 lists 
- Output: elements that are unique to the 1st input list
- Explicit Rules:
    - Calculate the elements that are unique to the 1st input list and return it 
- Implicit Rules
    - Return value is a set 
    - Assumption: lists will only contain hashable types
    - Assumption: if both input lists are empty, output will be an empty set.
    - Assumption: if the first input lists is empty, output will be an empty set.
- Questions:

EXAMPLES 
# 1) 
print(unique_from_first([3,6,9,12], [6,12,15,18]))
# {9, 3}

# 2)
print(unique_from_first([], [6,12,15,18]))
# set()

# 3)
print(unique_from_first([], []))
# set()

DATA STRUCTURES
Lists and sets

ALGORITHM
1. Convert both lists to sets
2. Calculate the difference between the sets: set 1 - set 2
3. Return the difference 

IMPLEM NOTES
- using subtraction operator? 
"""

def unique_from_first(list1, list2):
    return set(list1) - set(list2)


# 1) 
print(unique_from_first([3,6,9,12], [6,12,15,18]))
# {9, 3}

# 2)
print(unique_from_first([], [6,12,15,18]))
# set()

# 3)
print(unique_from_first([], []))
# set()

# 4)
print(unique_from_first([2, 3], [1]))
# set()