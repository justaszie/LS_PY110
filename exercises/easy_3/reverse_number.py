"""
PROBLEM
- Input: positive integer
- Output: integer - input number's digits reversed
- Explicit Rules: return the number that has the input's digits in the reverse order
- Implicit Rules:
    - 1-digit number input returns the same number
    - After reversing the digits, the result may have leading zeros. Those zeros should be dropped
- Questions: N/A

EXAMPLES
print(reverse_number(12345))    # 54321
print(reverse_number(12213))    # 31221
print(reverse_number(456))      # 654
print(reverse_number(12000))    # 21 # Note that leading zeros in the result get dropped!
print(reverse_number(1))        # 1

DATA STRUCTURES
- Integers
- Potentially, lists of digits or strings

ALGORITHM
1. Convert the number to a string
2. Reverse the string
3. Convert the new string to an integer 
"""

def reverse_number(number):
    result_str = str(number)[::-1]
    return int(result_str)

print(reverse_number(12345))    # 54321
print(reverse_number(12213))    # 31221
print(reverse_number(456))      # 654
print(reverse_number(12000))    # 21 # Note that leading zeros in the result get dropped!
print(reverse_number(1))        # 1