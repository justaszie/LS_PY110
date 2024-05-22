"""

PROBLEM
- Input: non-negative number (integer)
- Output: string representation of input number
- Explicit Rules:
    - Can't use any standard conversion (str, repr, implicit conversion with print, etc.)
- Implicit Rules:

EXAMPLES 
print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True

DATA STRUCTURES
- Integers for input, string for output
- Dictionary for mapping numbers to their string representation 

ALGORITHM:
1. Create integer to string dictionary
3. Assign input number value to "current number" variable
4. Set result string to empty string
5. While the current number is > 0: 
    A. get the last digit using formula [current_number % 10]]
    B. Convert the last digit to string value using mapping dictionary 
    C. Add the string value of the last digit to the 1st position of the result string
    D. reassign current number to its value divided by 10 (only integer part of divison)
6. Return the result string 



4321 should give iterations:
input number / 10**0 % 10. 1 = 4321 % 10     
input number / 10**1 % 10. 2 = 4321 / 10 % 10
3 = 4321 / 10 / 10 % 10
input number / 10**3 % 10. 4 = 4231 / 10 / 10 / 10 % 10 
4 / 10 = 0. STOP 

"""

def integer_to_string(number):
    STRING_VALUES = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
    }

    # if number == 0:
    #     return '0'
    

    result = ''

    current_number = number 
    while True:
        last_digit = current_number % 10
        result = STRING_VALUES[last_digit] + result
        current_number = current_number // 10
        if current_number == 0:
            break

    return result


print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True