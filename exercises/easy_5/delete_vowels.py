"""
PROBLEM
- Input: List of strings
- Output: List of same strings but with vowels removed
- Explicit Rules:
    - Return value list should have the same strings as the input list but the strings should not contain any vowels
    - 
- Implicit Rules:
    - Assuming empty input list = empty output list
    - Assuming no input validation required
    - Assuming empty strings in input list will remain empty strings in output list
    - If a string in input list has only vowels, it will be represented by an empty string in the output list
    - The vowel removal is case-insensitive (both lower and upper case vowels are removed)
    - Assuming that any special characters or punctuation will be included in the output strings
- Questions:
    - Return new value vs mutation. Assuming new value
    - Empty list. Assuming returns empty list
    - Empty strings in input list. 
    - Special characters

EXAMPLES
print(remove_vowels(['abcdefghijklmnopqrstuvwxyz']))        # ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(['green', 'YELLOW', 'black', 'white'])) # ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(['ABC', 'AEIOU', 'XYZ']))               # ['BC', '', 'XYZ']
print(remove_vowels(['', 'AEIOU', 'XYZ']))               # ['', '', 'XYZ']
print(remove_vowels([]))               # []


DATA STRUCTURES
Strings, lists 

ALGORITHMS
1. Create an empty result list 
2. Iterate over the input string values. For each string:
    [!] A. Create a new string with vowels removed from current string value
        - Create an empty no_vowels string
        - Iterate over each character of the original string. For each iteration:
            - If the current current character is not a vowel:
                - Add it to the end of the result string
        - Return the result string
    B. Addd the new string to the end of the result list 
3. Return the result list 

[!] Vowel removal can be a separate function 

IMPLEM NOTES
1. comprehension to create new string using list of characters? 
2. Vowels = 'aeiou'
"""

def get_no_vowels_string(string):
    vowels = 'aeiou'
    return ''.join([char for char in string if char.lower() not in vowels])

def remove_vowels(strings):
    return [get_no_vowels_string(s) for s in strings]

print(remove_vowels(['abcdefghijklmnopqrstuvwxyz']))        # ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(['green', 'YELLOW', 'black', 'white'])) # ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(['ABC1*', 'AEIOU', 'XYZ']))               # ['BC1*', '', 'XYZ']
print(remove_vowels(['', 'AEIOU', 'XYZ']))               # ['', '', 'XYZ']
print(remove_vowels([]))               # []