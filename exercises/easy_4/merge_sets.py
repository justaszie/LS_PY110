"""
PROBLEM
- Inputs: 2 lists 
- Output: a set that is a union of 2 sets, created from the input lists
- Explicit Rules:
    - Convert 2 lists to sets, create a union of the 2 and return it 
    - The result should be a new set value - not updating one of the sets created from lists 
- Implicit Rules:
    - Union = unique set of elements from both lists 
- Questions:
    - What type of elements can be in the lists. Assuming only hashable types allowed: imutable types (tuples only if they contain immutable types)
    - Assuming that the lists will contain a single type of element, not heterogenous types
    - Assuming empty lists returns empty set 

EXAMPLES
# 1)   
print(merge_sets([3,5,7,9], [5,7,11,13]))
# {3, 5, 7, 9, 11, 13}

# 2)
print(merge_sets([], []))
# {}

IMPLEM NOTES
.union mutating, | operator non mutating
Set can only contain hashable types. 

"""
def merge_sets(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    return set1 | set2 


print(merge_sets([3,5,7,9], [5,7,11,13]))
# {3, 5, 7, 9, 11, 13}

print(merge_sets([], []))
# {}

