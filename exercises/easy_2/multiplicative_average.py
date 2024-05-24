"""
PROBLEM
- Inputs: list of integers
- Outputs: string
- Explicit Rules:
    - Result is from multiple operations:
        1. Multiply all integers from the list together
        2. Divide the multiplication result by the number of elements
        3. Round up the result to 3 decimal place
        4. Return the result as a string
- Implicit Rules:
    - Assumption: empty list will return 0
    - Assumption: input will always be a list 
- Questions:
    - Return value for empty list?


EXAMPLES
# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")
print(multiplicative_average([]) == "0")

DATA STRUCTURES
- List as input
- Floats for operations
- String for return value 

ALGORITHM
1. If empty list, return "0"
2. Else, continue
[!] 3. Multiply all the elements of the list together and assign to multiplication variable
4. Divide the multiplication result by the number of elements
5. Round the division result up to 3 decimal places
6. Return the rounded up division value converted to string 

(3) Details:
1. If the list has only 1 element, return the 1st element. 
2. Set result to 1st element of the list 
3. Iterate over the list starting from the 2nd element. For each element:
    multiply the result by the current element
4. Return result

IMPLEM NOTES
- Rounding through formating vs math. First, will try formating with f-strings. 
If it doesn't work, I'll use math module. 

"""

def multiply(lst):
    result = lst[0]
    if len(lst) > 1:
        for element in lst[1:]:
            result *= element
    
    return result


def multiplicative_average(lst):
    if len(lst) == 0:
        return "0.000"

    multiplication = multiply(lst)
    division = multiplication / len(lst)
    return f"{division:.3f}"


# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")
print(multiplicative_average([0]) == "0.000")