"""
PROBLEM
- Input: 2 lists of integer (same length)
- Output: list where each element is product of corresponding elements from the 2 lists
- Explicit Rules: 
    - Return a list where each element is product of corresponding elements from the 2 lists
    - Both input lists are of same length
- Implicit Rules:
- Questions:
    - Assuming that the lists can be empty and the return value will be an empty list

EXAMPLES
print(multiply_elements([1, 2, 3], [4, 5, 6]))
# [4, 10, 18]

print(multiply_elements([], []))
# []

DATA STRUCTURES
lists

ALGORITHMS
1. Create empty result list 
2. Iterate over both lists at the same time For each pair of values:
    A. Calculate the prodct of the elements from the pair of values
    B. add the product to the result list 
3. return the result list 

IMPLEM NOTES
zip?
"""

def multiply_elements(list1, list2):
    return [number1 * number2 for number1, number2 in zip(list1, list2)]


print(multiply_elements([1, 2, 3], [4, 5, 6]))
# [4, 10, 18]

print(multiply_elements([], []))
# []