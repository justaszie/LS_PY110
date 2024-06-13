"""
PROBLEM
- Input: list 
- Output: new list
- Explicit Rules:
    - Don't modify the input list, return a new list value 
    - New list should have the same elements as input list but first element shouw be moved to last position
    - If input is empty list, return should also be empty list 
    - If input is not a list, return None 
- Implicit Rules:
    - 
- Questions:
    - List with one element, return a list with same element in same position 
    - If list contains nested data structures? should the return value be a deep copy? Assuming no

EXAMPLES
- provided 
DATA STRUCTURES
- Lists

ALGORITHM
1. If the input is not a list, return None
2. If the input is empty list or contains one element, return a copy of the input list
3. set temp variale to the first element of the list
4. remove the first element of the list 
5. Append the value assigned to temp variable to the end of the 

1. If the input is not a list, return None
2. If the input is empty list or contains one element, return a copy of the input list
3. create an empty result list 
3. Iterate over the index values of the  input list. For each value:
    - If index is 0, do nothing
    - If the index is > 0, append the lement to the result list.
4. Append the first element of the input list to the end of the result list. 
5. return the result list. 



"""
def rotate_list(input_list):
    if not isinstance(input_list, list):
        return None
    if len(input_list) in [0,1]:
        return input_list.copy()
    
    # V1 
    # result = []
    # for element in input_list[1:]:
    #     result.append(element)

    # result.append(input_list[0])

    # return result

    # V2
    return input_list[1:] + [input_list[0]]

    # V3
    # result = input_list.copy()
    # result.append(result.pop(0))
    # return result

# All of these examples should print True

print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
print(rotate_list(['a']) == ['a'])
print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
print(rotate_list([]) == [])

# return `None` if the argument is not a list
print(rotate_list(None) == None)
print(rotate_list(1) == None)

# the input list is not mutated
lst = [1, 2, 3, 4]
print(rotate_list(lst) == [2, 3, 4, 1])
print(lst == [1, 2, 3, 4])

