"""
PROBLEM
- Input: string
- Output: Length of the longest vowel substring
- Rules:
    - Input string will never be empty and will only contain lowercase alphabetic characters
    - Vowels of interest: ()"a", "e", "i", "o", and "u")
    -
- Questions:


ALGORITHM
1. Collect all vowel substrings
    A. Create an empty substrings list
    B. Set current substring to empty string
    C. Iterate over the characters of the string, keeping track of the index. On each iteration:
        If the current character is a vowel:
            - Append the current character to the end of the current substring
            - If it's the last character of the string:
                - Add the current substring to the list of strings
        Else the current character is not a vowel:
            - Add the current substring to the lsit of strings
            - Set the current substring to empty string
2. Find and return the max length (use comprehension to collect lengths and take max)


"""
def longest_vowel_substring(string):
    substrings = []
    current_sub = ''

    for idx, char in enumerate(string):
        if char in ("a", "e", "i", "o", "u"):
            current_sub += char
            if idx == len(string) - 1:
                substrings.append(current_sub)
        else:
            substrings.append(current_sub)
            current_sub = ''
    return max([ len(sub) for sub in substrings ])

print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)