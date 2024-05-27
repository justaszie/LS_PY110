"""
PROBLEM
- Input: 2 integers: count and start number of sequence
- Output: list with a sequence of numbers
- Explicit Rules:
    - Count (first argument) is always >= 0
    - if count input is 0, output is an empty list 
    - Starting number can be any integer 
    - Output sequence is built this way: 
        - List length = count argument
        - Each element is a multiple of the startign value argument 
- Implicit Rules:
    - The output elements: multiples of starting value means: 
        - 1st element = start value * 1
        - 2nd element = start value * 2
        etc.. 
- Questions: N/A 
    
EXAMPLES
print(sequence(5, 1))          # [1, 2, 3, 4, 5]
print(sequence(4, -7))         # [-7, -14, -21, -28]
print(sequence(3, 0))          # [0, 0, 0]
print(sequence(0, 1000000))    # []

DATA STRUCTURES
- Integers
- List
- Ranges

ALGORITHM:
- Create an empty list "sequence"
- Iterate through integer values from 1 until the value of 'count' argument, included. For each integer value:
    - Calculate the multiple value using this formula: {starting numer} * current iterator value
    - Append the multipel value to the sequence list
- return the sequence list


"""
def sequence(count, start_value):
    # result = []
    # for multiplier in range(1, count + 1):
    #     result.append(start_value * multiplier)
    
    # return result

    return [start_value * multiplier for multiplier in range(1, count + 1)]

print(sequence(5, 1))          # [1, 2, 3, 4, 5]
print(sequence(4, -7))         # [-7, -14, -21, -28]
print(sequence(3, 0))          # [0, 0, 0]
print(sequence(0, 1000000))    # []