"""
PROBLEM 
- Input: String 
- Output: List of substrings that can be created from the word
- Explicit Rules:
    - Each substring needs to start with the first letter of the string
    - The list of substrings should be sorted from shortest to longest before returning it
- Implicit Rules:
    - Assumption: the substrings should retain the casing of the original string
    - Assumption: empty string returns empty list
- Questions: 

EXAMPLES
print(leading_substrings('abc'))      # ['a', 'ab', 'abc']
print(leading_substrings('a'))        # ['a']
print(leading_substrings('xyzzy'))    # ['x', 'xy', 'xyz', 'xyzz', 'xyzzy']
print(leading_substrings(''))         # []

DATA STRUCTURES
Strings and lists 

ALGORITHM
Note: Start with the first letter, iterate over remaining letters and store a string at each iteration

1. Create an empty list "substrings"
2. Set first character to the first character of the input string
3. Iterate over the indexes of the characters in the input string, starting from the value 1 (second character) up until value = number of elements in input list. On each iteration
    A. Create a string that is a part of the input string, 
    starting from the 1st character up to the character positioned at current index (excluded)
    B. Add the created string to the substrings list 
4. Sort the substrings list based on the length of each substring, sorted in ascending order.
5. Return substrings list 

    

Note: one character - add it to the list before loop? 
IMPLEM NOTES
- Sort using len function
"""

def leading_substrings(string):
    return sorted([string[0:idx] for idx in range(1, len(string) + 1 )], key=len)

    # substrings = []
    
    # for idx in range(1, len(string) + 1):
    #     substrings.append(string[0:idx])
    
    # substrings.sort(key = len)

    # return substrings


print(leading_substrings('abc'))      # ['a', 'ab', 'abc']
print(leading_substrings('a'))        # ['a']
print(leading_substrings('xyzzy'))    # ['x', 'xy', 'xyz', 'xyzz', 'xyzzy']
print(leading_substrings(''))         # []