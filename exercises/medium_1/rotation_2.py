"""
PROBLEM 
- Inputs:
    - A number
    - An integer that represents the number of digits to rotate
- Output:
    - New number with {count} last digits rotated
- Explicit Rules:
    - Rotation means that the first of the digits to be rotated is moved to the very end of the number
- Implicit Rules:
    - If count = 1, there are no changes. return same number
- Questions:
    - Count is higher than total digits in the number? 
        - Assuming that we return the same value 
    - Count = total digits in the number
    - Count = 0, return same number
    - Assuming that count is non negative 
    - Assuming number is non negative

Overall logic:
- Take subset of digits X last digits
- Take the 1st digit of the subset and move to the very end of the number

EXAMPLES
print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True

DATA STRUCTURES
String, list of characters as interim

ALGORITHM
1. If count < 2 OR if count > total digits in the number:
    return same value 
2. Convert the number to a string
3. Set cutoff_index to (length of string - {count})
3. Take a subset of the string starting from the (cutoff_index + 1) - nth character until the end.
4. Create a new string from the following components:
    A. Original string from first character up to cutoff_index, excluded
    B. Substring from second character to the end 
    C. first character of the substring
5. Convert the new string to integer value
6. Return the integer value



IMPLEM NOTES
- to get number of digits to str conversion and use len


"""

def rotate_rightmost_digits(number, count):
    if count < 2 or len(str(number)) < count:
        return number
    
    number_str = str(number)
    cutoff_idx = len(number_str) - count

    rightmost = number_str[cutoff_idx:]

    result_str = f"{number_str[:cutoff_idx]}{rightmost[1:]}{rightmost[0]}"

    return int(result_str)


print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True