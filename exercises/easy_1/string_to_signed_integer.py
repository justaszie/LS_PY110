"""

PROBLEM
- Inputs: string representing a signed number
- Outputs: integer - numeric value of the number (positive or negative)
- Explicit Rules:
    - if the number is preceded by a "-", return negative number
    - if the number is preceded by + OR no leading sign, return positive number
    - String always contains a valid number. No input validation needed
    - Function can't use any standard conversion functions (e.g. int)
    - We can use the string_to_integer function developed previously 

- Implicit Rules:
    - The number can be 0 

- Questions:
    - can it be 0? 

EXAMPLES
print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True

DATA STRUCTURES
- Strings (input)
- Integers (output)


ALGORITHM
1. Capture the 1st character of the input string
2. If the 1st character is "-":
        return the value of string_to_integer(input string from 2nd character onwards), multiplied by -1 
    else if the 1st character is "+"
        return the value of string_to_integer(input string from 2nd character onwards)
    else:
        return the value of string_to_integer(input string)

"""

def string_to_integer(number_string):
    DIGITS = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
    }
    
    total = 0

    for idx in range(len(number_string)):
        current_number = DIGITS[number_string[len(number_string) - 1 - idx]]
        result_value = current_number * 10**idx
        total += result_value
    
    return total

def string_to_signed_integer(number_string):
    first_char = number_string[0]
    match first_char:
        case '-':
            return -1 * string_to_integer(number_string[1:])
        case '+': 
            return string_to_integer(number_string[1:])
        case _:
            return string_to_integer(number_string)


print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True