"""
PROBLEM
- Input: 2 lists 
- Output: frozenset containing common elements of the 2 input lists
- Exlicit Rules:
    - Transform the input lsits to frozentset objects
    - Create and return a frozenset object that contains the common element(s) from the 2 input lists
- Implicit Rules:
- Questions:
    - Assumption input lists will only contain hashable elements
    - Assumption empty lists will result in empty frozenset

EXAMPLES
print(find_intersection([2,4,6,8], [1,3,5,7,8]))
# frozenset({8})

print(find_intersection([], []))
# frozenset({8})

DATA STRUCTURES

ALGORITHM 
1. Convert list 1 to a frozenset 1
2. Convert list 2 to a frozenset 2
3. Calculate and return the intersection of the 2 sets 

Implem Notes

"""
def find_intersection(list1, list2):
    return frozenset(list1) & frozenset(list2)


print(find_intersection([2,4,6,8], [1,3,5,7,8]))
# frozenset({8})

print(find_intersection([], []))
# frozenset({8})