"""
PROBLEM
- Input: List
- Output: Input list reversed in place (same object, mutated)
- Explicit Rules:
    - The function reverses the order of the input list's elements
    - The function mutates the input list in place - it doesn't create new objects 
- Implicit Rules:
    - The function returns the value of the input list, after reversing the order
    - If the list is empty or contains one element,
      the function returns the same value with no changes
- Questions: 

EXAMPLES 
- Provided

DATA STRUCTURES
- Lists

MENTAL MODEL NOTES

Either 
A) Go through the list, take the element in the opposite index (last index - current index), remove it and insert it at the beginning
# above seems dangerous as we're mutating the list (removing elements) while iterating
B) Go through the list in reverse oder, remove the element and insert it at the beginning.

WON'T WORK = the next to last would be inserted before last (same order as input)

Input index: [0, 1, 2]
1. insert 0 at the end -1 
2. insert 1 at the end - 1 = -1 - 1  
3. insert 2 at the end - 2 = -1 -2... 
....
4. Delete the original members 0-2. 0:original_len.
    - iterate from index 0 to 
Output index:  [2, 1, 0]


SCRATCH 
. Iterate from last index to first index. 
- For each index, append the corresponding element to the end. 
- iterate through index 0 to len(original list) (excl), remove the element 

ALGORITHM
1. Assign original list length to "original len" variable
2. Iterate through the elements of the input list in the reverse order. For each element
3. Append it to the input list
4. Iterate through index values from 0 up to origina len value (excl). For each index
    - Remove the element of the input list positioned at the current index value
5. Return original list 

""" 

def reverse_list(input_list):
    original_length = len(input_list)
    for element in input_list[::-1]:
        input_list.append(element)
    
    for index in range(0, original_length):
        input_list.pop(0)
    
    return input_list


list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result)  # prints [4, 3, 2, 1]
print(list1 is result)  # prints True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2)  # prints ['e', 'd', 'c', 'b', 'a']
print(list2 is result2)  # prints True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3)  # prints ['abc']
print(list3 is result3)  # prints True

list4 = []
result4 = reverse_list(list4)
print(result4)  # prints []
print(list4 is result4)  # prints True