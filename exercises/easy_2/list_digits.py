"""
PROBLEM
- Inputs: a positive integer (> 0)
- Outputs: List of digits in the number
- Explicit Rules: Return the list of digits that compose the input number
- Implicit Rules: One digit number returns a list of one element

EXAMPLES
print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True

DATA STRUCTURES
- Integer, List

ALGORITHM
# Decided to do it the hard way for the lulz
1. create an empty list - digits
2. while input number > 0 perform the following:
    A. perform modulo 10 operation on input number
    B. prepend the result of modulo operation to the list of digits 
    C. reassign input number to input number / by 10 (only integer part)
3. return the digits list 

IMPLEM NOTES
- loop and peform modulo until 0 
- type coercion: convert to string and convert to list 
"""

def digit_list(number):
    digits = []

    while number > 0 :
        digits.insert(0, number % 10)
        number //= 10
    
    return digits

def digit_list_v2(number):
    return list([int(digit) for digit in str(number)])

print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True


print(digit_list_v2(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list_v2(7) == [7])                       # True
print(digit_list_v2(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list_v2(444) == [4, 4, 4])               # True