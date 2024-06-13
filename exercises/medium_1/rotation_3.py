"""
PROBLEM
- Input: Integer Number 
- Output: maximum rotation of the input 
- Explicit Rules:
    - Use rotate_rightmost_digits 
    - Maximum rotation logic. E.g. 6 digit number 735291 
        1. Move the 1st digit to the end
        2. Keep the 1st digit and move the 2nd digit to the end 
        3. Keep 1st and 2nd digits and move the 3rd to the end
        4. Keep the first 3 digits and move the 4th to the end
        5 Keep the first 4 digits and move the 5th to the end. 
        .... 
- Implicit Rules:
    - 1 digit => no changes 
    - 2 digits => 1 rotation 
    - If ending number begins with leading 0s, the 0s are dropped in the returned number 

- Questions:
    - Assuming only non-negative integers
- Mental model: 
    - Number of rotations = total digits - 1
    - On each rotation we take i + 1 - th character and move it to the end. i starts with 0 and ends with 4 (incl)




735291 
=> 352917
=> 329175 
=> 321759 
=> 321597 
=> 321579

EXAMPLES 
print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True
print(max_rotation(105) == 15)                 # True

DATA STRUCTURES


ALGORITHM 
1. Iterate through values from 0 to total digits - 1, excluded. For each value N:
    A. set number to number after rotating (total digits - N) rightmost elements
2. Return the number 


- 2 digits 35.
    - N = 0 
    - Rotate 2 - 0 rightmost values 
    - Number = 53-
- 1 digit: 0 rotations 0,

IMPLEM NOTES
"""
def max_rotation(number):
    number_str = str(number)
    total_digits = len(number_str)
    for i in range(0, total_digits - 1):
        number_str = str(rotate_rightmost_digits(int(number_str), total_digits - i))

    return int(number_str)


def rotate_rightmost_digits(number, count):
    if count < 2 or len(str(number)) < count:
        return number
    
    number_str = str(number)
    cutoff_idx = len(number_str) - count

    rightmost = number_str[cutoff_idx:]

    result_str = f"{number_str[:cutoff_idx]}{rightmost[1:]}{rightmost[0]}"

    return int(result_str)

print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True
print(max_rotation(105) == 15)                 # True