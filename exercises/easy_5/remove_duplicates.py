"""
PROBLEM
- Input: Sequence of integers 
- Output: list / tuple, depending on input type 
- Explicit Rules:
    - Remove the elements where same value appears successfully. 
    E.g. if number 1 appears 3 times in succession, only the 1st one will be included in the return value\
- Implicit Rules: 
    - 
- Questions:
    - Assuming sequence can be list or tuple
    - Assuming we return new object (esp. relevant if input is a tuple )
    - Assuming return value data type is the same as input (list if list, tuple if tuple)
    - Assuming empty list / tuple returns empty list / tuple 

EXAMPLES
original = [1, 1, 2, 3, 3, 3, 4, 5, 5, 6, 6, 6]
expected = [1, 2, 3, 4, 5, 6]
print(unique_sequence(original) == expected)      # True

DATA STRUCTURES
Lists / tuples 

ALGORITHM
1. Create an empty result list
2. Iterate over the input sequence. For each value:
    A. If the results list is empty or current value does not equal the last element of result list:
        - append the current element to the result list
3. Convert the result list to the relevant data type, depending on input data type
4. Return the result in the relevant data type

IMPLEM NOTES
Do for list first, then make it generic
Alternative approach: go through elements from 1 to end. If it's different from previous element OR it's last element, keep it
"""

def unique_sequence(sequence):
    # V1
    # result = []
    # for element in sequence:
    #     if not result or element != result[-1]:
    #         result.append(element)
    
    # return result 

    # V2
    result = [elem for idx, elem in enumerate(sequence) if idx == 0 or elem != sequence[idx - 1]]
    # for idx, elem in enumerate(sequence[1:]):
    #     if idx == 0 or idx == (len(sequence) - 1 or 
    return result 


original = [1, 1, 2, 3, 3, 3, 4, 5, 5, 6, 6, 6, 8]
expected = [1, 2, 3, 4, 5, 6, 8]
print(unique_sequence(original))
print(unique_sequence(original) == expected)      # True

