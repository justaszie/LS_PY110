"""
PROBLEM
- Input: a number (int)
- Output: next featured number (int)
- Rules:
    - featured number:
        - odd number
        -  multiple of 7
        - all digits only occur once
    - next featured number > input number
    - if no next featured number, return error message  "There is no possible number that "
         "fulfills those requirements."
    - Maximum featured number is 9876543201. I.e. if input is >= 9876543201, return error message
- Questions:
    -

ALGORITHM
1. If input number >= max ft number (9876543201), return error message
"There is no possible number that fulfills those requirements."
2. iterate over all integer values, starting from the input number (excl.) up to the max ft number (incl.).
For each value:
    A. return the current integer value if it fits the conditions:
        i. it's odd (there is a remainder when divided by 2)
        ii. it's multiple of 7 (no remainder after dividing by 7)
        ii. digits only appear once. [!]

[!] determining repeated numbers.
1. convert number to a string
2. Create an empty digits set
3. iterate over all characters of the number, converted to string
    A. if the digit (char) is already in the digits set, return True (meaning duplicated number)
    B. Add the current character to the set
4. Return False after the iteration is over

IMPLEM NOTES

"""

def repeated_digits(number):
    digits = set()

    for digit in str(number):
        if digit in digits:
            return True
        digits.add(digit)

    return False

def is_featured(number):
    max_featured = 9876543201

    if number >= max_featured:
        return ("There is no possible number that "
         "fulfills those requirements.")

    for next in range(number + 1, max_featured + 1):
        if next % 2 == 1 and next % 7 == 0 and not repeated_digits(next):
            return next


print(is_featured(12) == 21)                  # True
print(is_featured(20) == 21)                  # True
print(is_featured(21) == 35)                  # True
print(is_featured(997) == 1029)               # True
print(is_featured(1029) == 1043)              # True
print(is_featured(999999) == 1023547)         # True
print(is_featured(999999987) == 1023456987)   # True
print(is_featured(9876543186) == 9876543201)  # True
print(is_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(is_featured(9876543201) == error)       # True