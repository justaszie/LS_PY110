"""
PROBLEM
- Input: string 
- Output: boolean (True if palindrome, False otherwise)
- Explicit Requirements:
    - Palindrome is string that is same read forwards and backwards
    - Comparison is case in-sensitive ("Madam" is considere as palindrome)
    - Comparison ignores all non-alphanumeric characters ("Madam, I'm Adam" is palindrom. ' is ignored)

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
        - assigned processed_string to the original string, converted to lowercase
          and with all non-alphanumeric characters removed.
        - If processed string is palindrome (subprocess - already done before), return true
            else, return false 


"""

def is_palindrome(string):
    return string and string == string[::-1]

def is_real_palindrome(string):
    processed_str = ''.join([
        char for char in string.casefold() if char.isalnum()
    ])

    return is_palindrome(processed_str)

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True