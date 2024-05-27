"""
PROBLEM
- Input: 2 lists with numbers
- Output: List with product of the numbers positioned at the respective indexes of both lists
- Explicit Rules:
    - Result list has product of the elements that are at the same index in list1 and list2
    - The lists will have the same number of elements
- Implicit Rules:
    - Assumption: the input lists contain integers only
    - Assumption: Empty lists in input return empty list 
- Questions
    - Empty lists
    - Numbers = Only integers? 

EXAMPLES
1) 
list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True

2)
list1 = []
list2 = []
print(multiply_list(list1, list2) == []])  # True

DATA STRUCTURES
- Lists

ALGORITHM
1. Create an empty list - products
2. Iterate over both lists at the same time. For each pair of elements:
    A. Calculate the product of both elements
    B. Append the product to the products list 
3. Return the products list 
"""

def multiply_list(list1, list2):
    products = []

    for element1, element2 in zip(list1, list2):
        numbers = element1 * element2
        products.append(numbers)

    return products


# 1) 
list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True

# 2)
list1 = []
list2 = []
print(multiply_list(list1, list2) == [])  # True