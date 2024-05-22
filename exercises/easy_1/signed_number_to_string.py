"""
PROBLEM
- Input: any integer (positive or negative)
- Output: string representation of the input number
- Explicit Rules:
    - Can't use any built in conversion features
    - Can use integer_to_string function 
- Implicit Rules:
    - If the number is positive, string must have a leading + character
    - If the number is negative, string must have a leading - character
    - 0 number has no leading character 

EXAMPLES 
print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True

DATA STRUCTURES
integers for input, strings for output.
reusing existing integer_to_string function 

ALGORITHM.
integer_to_string returns a string from a positive number or 0. 

1. If the number is greater than  0:
        - get the result of calling integer to string and assign it to result string
        - prepend + sign to result string
        - return result
    Else if the number is less than 0:
        - get the result of calling integer to string with absolute value of input number as argument, and assign it to positive_str
        - prepend - sign to result string 
        - return result
    else:
        - return '0'


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

def signed_integer_to_string(number):
    if number > 0:
        return '+' + integer_to_string(number)
    elif number < 0:
        return '-' + integer_to_string(abs(number))
    else:
        return '0'
    
print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True
    