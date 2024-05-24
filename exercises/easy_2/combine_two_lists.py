"""
PROBLEM
- Inputs: 2 lists
- Outputs: 1 list combining elements from both lists 
- Explicit Rules:
    - In result list, the elements from both input lists are alternated. I.e. 
    [list 1 element, list 2 element, list 1 element, etc.]
    - Both lists will not be empty
    - Both lists are of equal lengths
- Implicit Rules: N/A
- Questions: N/A 

EXAMPKLES
Provided

DATA STRUCTURES
Lists

ALGORITHMS:
1. Create an empty result list 
2. Iterate over index values from 0 until length of input list 1 (excluded). For each index value:
    - Append the element positioned at the current index from input list 1 to the result list 1 
    - Append the element positioned at the current index from input list 1 to the result list 2
3. Return result list.

IMPLEMENTATION
- A: iterate over indexes
- B: Using zip to iterate over both lists and assign both elements
"""

def interleave(list1, list2):
    result = []
    for pair in zip(list1, list2):
        result.extend(pair)
    return result


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True