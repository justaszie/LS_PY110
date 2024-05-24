"""

PROBLEM
- Inputs: 2 lists
- Outputs: Set that is a union of both lists 
- Explicit Rules:
    - Both arguments will always be lists. 
    - Result is a set that combines the elements from both lists without repeating them.
- Implicit Rules:
    - Assumption on empty list(s): 
        - Both empty lists = empty set
        - One empty list = set with the elements from the other list only
    - Assumption: there will not be heterogenous lists (multiple data types)
    - Assumption: lists will only contain elements with hashable data types. 
- Questions:
    - Empty list(s)
    - Heterogenous lists
    - Hashable data types 
    - Are we allowed to mutate the arguements? 

EXAMPLES
    - [1, 3, 5], [3, 6, 9] => {1, 3, 5, 6, 9}
    - [], [1, 3, 5] => {1, 3, 5}
    - [], [] => {}

DATA STRUCTURES
    - Lists and sets 
    - Only hashable types

ALGORITHM:
1. Create empty result set
2. Loop through list 1 arguments. For each element:
    - Add the element to the result set (Set will take care of uniqueness automatically)
2. Loop throuth list 2 argument. For each element:
    - Add the element to the result set (Set will take care of uniqueness automatically)
3. Return the result set.
"""

def union(list1, list2): 
    result = set()

    for element in list1:
        result.add(element)
    for element in list2: 
        result.add(element)

    return result 

def copy_non_dups_to(result_set, lst):
    for value in lst:
        result_set.add(value)

def union2(list1, list2):
    result_set = set()
    copy_non_dups_to(result_set, list1)
    copy_non_dups_to(result_set, list2)
    return result_set

# print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True
# print(union([], [3, 6, 9]) == {3, 6, 9}) # True
# print(union([3, 6, 9], []) == {3, 6, 9}) # True
# print(union([], []) == set()) # True

print(union2([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True