"""
PROBLEM
- Input: positive integer
- Output: integer (sum of input number's digits)
- Explicit Rules:
    - Input intiger is positive.
    - Output is the sum of the input integer's digits
- Implicit Rules:
    - Assuming that positive integer means non-negative - i.e. can be zero 
- Questions: 
    - Assuming that positive integer means non-negative - i.e. can be zero 

EXAMPLES
print(sum_digits(23))           # 5
print(sum_digits(496))          # 19
print(sum_digits(123456789))    # 45
print(sum_digits(2))    # 2

DATA STRUCTURES
integers

ALGORITHM
1. Set sum to 0 
2. Loop while input number is > 0. On each iteration:
    A. set last digit to input number % 10
    B. Increment the sum value by the last digit
    C. set input number to input number / 10
3. Return sum value 

IMPLEM NOTES
% 10 while number > 0 ?
"""

def sum_digits(number):
    # V1 
    # sum = 0
    
    # while number > 0:
    #     last_digit = number % 10
    #     sum += last_digit
    #     number = number // 10
    
    # return sum

    # V2 
    return sum([int(char) for char in str(number)])


print(sum_digits(23))           # 5
print(sum_digits(496))          # 19
print(sum_digits(123456789))    # 45
print(sum_digits(2))    # 2