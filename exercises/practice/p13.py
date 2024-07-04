"""
PROBLEM
- Input: 2 strings
- Output: True / False
- Rules:
    - Output True if some characters of 1st string can be rearranged to match 2nd str. False if not.
    - both strings only contain lowercase alphabetic letters. Strings won't be empty
- Questions:

ALGORITHM.
1. Start with list of characters in str1
2. Iterate over characters in str2. On each iteration
    A. If the current character of str2 is in the list of str1 characters:
        - Remove the character from str1
    B. Else:
        - Return False ()
3. return True (we went through the whole str2 and all characters were found in str1)
"""

def unscramble(scrambled, str_to_match):
    scrambled_chars = list(scrambled)
    for char in str_to_match:
        if char in scrambled_chars:
            scrambled_chars.remove(char)
        else:
            return False
    return True

print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == True)
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)