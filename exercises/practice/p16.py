"""
PRODUCT
- Input: string
- Output: int  - count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once
- Rules:
    - Input string only contains alphanumeric characters
    - Matching is case insensitive. if we have 'z' and 'Z', 'z' counts as a character that appears more than once

- Questions:

ALGORITHM
1. count the occurences of each character
    - Iterate over the string. For each character
    - Add the lowercase version of the character to 'counts' dictionary OR increment its count
2. Filter the counts to keep only the characters that have > 1 occurence
    - comprehension to keep a list of keys where value > 1
3. Return the number of remaining characters
"""

def distinct_multiples(string):
    counts = {}
    for char in string:
        counts[char.lower()] = counts.get(char.lower(), 0) + 1
    repeated = [ char for char, count in counts.items() if count > 1 ]
    return len(repeated)


print(distinct_multiples('xyz') == 0)               # (none)
print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
print(distinct_multiples('unununium') == 2)         # u, n
print(distinct_multiples('multiplicity') == 3)      # l, t, i
print(distinct_multiples('7657') == 1)              # 7
print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5