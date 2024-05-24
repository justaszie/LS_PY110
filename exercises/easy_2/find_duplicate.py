"""
PROBLEM
- Inputs: Unordered list
- Outputs: The value that occurs twice 
- Explicit Rules:
    - One (and only one) of the values occurs twice 
    - All the other values occurs only once. 
- Implicit Rules:
    - Assumption: if the list only has 2 elements, it will be the same value repeated twice. We will return the value
    - Assumption: list can't have less than 2 elements. 
    - Assumption: same value can't occur 3 or more times
- Questions:
    - Edge cases: 
        - List with 2 elements
        - List with less than 2 elements

EXAMPLES
- Provided 
- Additional test case:
    - [2, 2] => 2

DATA STRUCTURES
- List 

ALGORITHM
1. Loop through the input list. For each element:
    - Count the number of occurences of that element in the list
    - If the number of occurences > 1,
        - Stop search and return the element.
    - else:
        - Continue iterating
"""

def find_dup(input_list):
    for element in input_list:
        if input_list.count(element) > 1:
            return element
    

print(find_dup([1, 5, 3, 1]) == 1) # True
print(find_dup([
                  18,  9, 36, 96, 31, 19, 54, 75, 42, 15,
                  38, 25, 97, 92, 46, 69, 91, 59, 53, 27,
                  14, 61, 90, 81,  8, 63, 95, 99, 30, 65,
                  78, 76, 48, 16, 93, 77, 52, 49, 37, 29,
                  89, 10, 84,  1, 47, 68, 12, 33, 86, 60,
                  41, 44, 83, 35, 94, 73, 98,  3, 64, 82,
                  55, 79, 80, 21, 39, 72, 13, 50,  6, 70,
                  85, 87, 51, 17, 66, 20, 28, 26,  2, 22,
                  40, 23, 71, 62, 73, 32, 43, 24,  4, 56,
                   7, 34, 57, 74, 45, 11, 88, 67,  5, 58,
              ]) == 73)       # True
