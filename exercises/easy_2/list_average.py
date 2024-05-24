"""
PROBLEM
- Inputs: List of integers 
- Outputs: Integer - average of integers in the list
- Explicit Rules:
    - The result should be rounded down to the integer component of the mathematical avreage (mean). E.g. 25.89 => 25
    - The list will not be empty
    - All elements in the list are positive integers
- Implicit Rules: N/A
- Questions: N/A 

EXAMPLES 
print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True

DATA STRUCTURES 
List
Floats
Integers

ALGORITHM 
1. Calculate the sum of all integers.
    - Set the sum to 0
    - Loop through the list and add each eleemnt to the sum 
2. Calculate float average by dividing the sum by the number of elements in the list
3. Return the integer component of the float average

"""
def average(numbers):
    # V1
    # numbers_sum = sum(numbers)
    # average = numbers_sum / len(numbers)
    # return int(average)

    # V2
    # return int(sum(numbers) / len(numbers))

    # V3
    return sum(numbers) // len(numbers)


print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True
