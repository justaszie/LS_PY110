"""

PROBLEM 
- Inputs: string of digits
- Outputs: number as integer
- Explicit Rules:
    - Can't use any standard python conversion functions 
    - All characters are numeric. There are no + or - leading signs
- Implicit Rules:
    - Assuming there are no empty strings
- Questions: N/A

4321 = 1 * 10**0 + 2 * 10**1 + 3 * 10**2 + 4*10**3

DATA STRUCTURES:
- Strings and integers

EXAMPLES: 
print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True

ALGORITHM
1. set total integer to 0 
2. Loop through string character indexes from 0 up to the highest index value. For each value:
    A. assign current character to the character located at the opposite index to the current number value. 
        E.g. for a string 875, if the current iteration number is 0, the digit value is at the index (2-0) - i.e. '5'.
    B. Convert the current character to numerical value.
    C. Calculate it's result value using the formula:
        result value = digit * 10**{current index}
    D. Add result value to the total integer
3. Return the total integer


- Further Exploration - 
Write a hexadecimal_to_integer function that converts a string representing a
 hexadecimal number to its integer value. 
 Hexadecimal numbers use base 16 instead of 10,
   and the characters A, B, C, D, E and F 
   (and the lowercase equivalents) correspond to decimal values of 10-15.


1. Create a dictionary mapping all possible characters to their numeric value.
2. All remaining process as strings_to integer with one modification.
    - Before getting numeric value, convert the character to lowercase
    - The formula for current number's value is changed:
        result value = digit * 16**{current index}
"""

def hexadecimal_to_integer(number_string):
    NUMBERS = {
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
        'a': 10,
        'b': 11,
        'c': 12,
        'd': 13,
        'e': 14,
        'f': 15,
    }

    total = 0

    for idx in range(len(number_string)):
        current_digit = NUMBERS[number_string[len(number_string) - 1 - idx].lower()]
        result_value = current_digit * 16**idx
        total += result_value
    
    return total



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

# print(string_to_integer("4321") == 4321)  # True
# print(string_to_integer("570") == 570)    # True

print(hexadecimal_to_integer('4D9f') == 19871)  # True
