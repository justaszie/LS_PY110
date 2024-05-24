"""
PROBLEM
- Inputs: list 
- Outputs: List with 2 lists - input elements split in 2 lists: 
- Explicit Rules:
    - Result list has 2 lists in it. The input list is split into 2 even sub-lists. 
    - If the input list has odd number of elements, the middle element is in the 1st sub-list
- Implicit Rules:
    - Empty list will return a list with 2 empty lists in it 
    - Input list with only 1 element will return a list where :
        - the only element is in the 1st list and 
        - the 2nd list is empty
- Questions: 
    - 

EXAMPLES 
# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]]) # Even number 
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]]) # Odd number
print(halvsies([5]) == [[5], []]) # One element 
print(halvsies([]) == [[], []]) # Empty list 


DATA STRUCTURES
- List for input
- Nested lists for output 

ALGORITHM
1. Create 2 empty lists: half1 and half2
2. Create a result list and add append half1 and half2 lists to it.
3. Calculate the appropriate middle index.
    - If list has odd number of elements. Middle index is that of the middle element
4. place the elements in appropriat half1 and half2 lists:
    - Half1 elements from indexes 0 to {middle index}, excluded 
    - Half2 elements from indexes {middle index} to {input list length}
5. Return the result list

4 elements - indexes 0-3 | Middle index = 4/2 = 2 | Halves = [0:2] (0,1) and [2:4] (2,3)
5 elements - indexes 0-4 | Middle index = 5/2 = 2.5 | Halves = [0:3] (0,1,2) and [3:5] (3, 4)
=> A: round the middle index up 
=> B: If the length is odd: middle index = len / 2 + 1. Else: middle index + 

Edge cases:
- lenght = 0. The halves will be [0:0] so nothing will be added 
- Length = 1. Middle index = 1 | halves = [0:1] (element 0) and [1:1] (nothing)
""" 

def halvsies(lst):
    even_length = len(lst) % 2 == 0
    middle_index = len(lst) // 2 if even_length else len(lst) // 2 + 1
    
    half1 = lst[:middle_index]
    half2 = lst[middle_index:]

    return [half1, half2]

# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])

# Q: What will happen with empty list (2 halves of 0:0)
# A: [0:0] slice creates an empty list. Results as expected: 2 empty lists. 