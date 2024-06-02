"""
PROBLEM
- Input: string
- Output: list of substrings
- Explicit Rules:
    - The output list of substrings should be orered by where in the string it begins. 
    E.g. in 'abc', the 'ab' would be before 'bc'
    - For multiple substrings that start at the same index, they should be ordered by their length.
    in ascending order 
    - Use leading_substrings function 
- Implicit Rules:
    - Assumptions:
        - If input is empty string, output is empty list
        - Upper / lower case of characters should be preserved
- Questions:
    - Empty string
    - one character 
    - case 

EXAMPLES

print(substrings('a'))
# prints ['a']

print(substrings('abcde'))

# prints
# [ "a", "ab", "abc", "abcd", "abcde",
#  "b", "bc", "bcd", "bcde",
#  "c", "cd", "cde",
#  "d", "de",
#  "e" ]

DATA STRUCTURES
Strings and lists 

ALGORITHM
1. Create an empty list "result"
2. Iterate over all indexes of the input string. For each index value 
    A. Get all substrings that start with the character positioned at the current index value.
    B. Add all the above substrings to the result list
3. Return the result list 

IMPLEM NOTES
"""
def leading_substrings(string):
    return sorted([string[0:idx] for idx in range(1, len(string) + 1 )], key=len)

def substrings(string):
    result = []
    for idx in range(len(string)):
        result.extend(leading_substrings(string[idx:]))
    
    return result


print(substrings('a'))
# prints ['a']

print(substrings('abcde'))

# prints
# [ "a", "ab", "abc", "abcd", "abcde",
#  "b", "bc", "bcd", "bcde",
#  "c", "cd", "cde",
#  "d", "de",
#  "e" ]