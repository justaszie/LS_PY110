"""
PROBLEM
- Input: String
- Output: List of palindromic substrings from the input string
- Explicit Rules:
    - Palindromic substrings: sequences of characters that read the same forward and backward
    - The output list must be sorted by order of appearance in the input string
    - Output list should include duplicates, if any.
    - Use "Substrings" function
    - Palindromes detection should be case sensitive:
        - AbcbA is palindromic
        - Abcba is not palindromic due to case
    - Special chaaracters should be considered when considering palindromes
    - Single characters are not palindromes
- Implicit Rules:
    - If no palindromes found, return empty list 
    - Assuming that empty input string = empty list 
- Questions:


EXAMPLES
- Provided

DATA STRUCTURES
- Strings, list 

ALGORITHMS
1. Create empty list "result"
2. Get all substrings of the input string
3. Iterate over each substring. For each iteration:
    A. If the substring is a palindrome: 
        - add it to the result list 
4. Return the result list. 

IMPLEM NOTES
- palindromic: string == string in reverse
- Substrings are extracted from left to right so the list should be sorted by the order of appearance already. 
"""

def is_palindrome(string):
    return len(string) > 1 and string == string[::-1]

def leading_substrings(string):
    return sorted([string[0:idx] for idx in range(1, len(string) + 1 )], key=len)

def substrings(string):
    result = []
    for idx in range(len(string)):
        result.extend(leading_substrings(string[idx:]))
    
    return result


def palindromes(string):
    # result = []
    # substrings_list = substrings(string)
    # for sub in substrings_list:
    #     if is_palindrome(sub):
    #         result.append(sub)
    
    # return result 

    return [sub for sub in substrings(string) if is_palindrome(sub)]

print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True
