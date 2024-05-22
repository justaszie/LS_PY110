"""
PROBLEM
- Input: string 
- Output: boolean (True if palindrome, False otherwise)
- Explicit Requirements:
    - Palindrome is string that is same read forwards and backwards
    - Comparison is case sensitive
    - All characters matter (no characters are excluded from comparison)

- Implicit Requirements: 
    - Assumption that empty string is NOT palindrome
    - Assumption that input will always be string 
    - Assumption that string is minimum 1 char long to be palindrome 
    - Numbers and special characters are allowed

- Questions: 
    - What should we return in case of empty string? 
    - What is minimal length for string

DATA STRUCTURES
boolean (True / False)

Algorithm:
- if string is not empty:
        - If string equals reverse string: return True.
            Else, return false 
    else, return false


"""

def is_palindrome(string):
    return string and string == string[::-1]

# All of these examples should print True

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)