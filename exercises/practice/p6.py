"""
PROBLEM
- Input: string
- Output: dict representing how many times each lowercase letter occurs in the strin
- Rules:
    - Only count lowercase letters. Ignore uppercase letters and non-letter characters
    - Empty string => empty dict
    - No lowercase letters => empty dict
- Questions

ALGORITHM
1. Create empty "counts" dictionary
2. Iterate over the input string, char by char. On each iteration
    - If the char is a lowercase letter:
        - Increment its count or add it to dictionary with '1' count
3. Return the counts dictionary




"""

def count_letters(string):
    counts = {}

    for char in string:
        if char.islower():
            counts[char] = counts.get(char, 0) + 1

    return counts


expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
print(count_letters('woebegone') == expected)

expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
            'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
print(count_letters('lowercase/uppercase') == expected)

expected = {'u': 1, 'o': 1, 'i': 1, 's': 1}
print(count_letters('W. E. B. Du Bois') == expected)

print(count_letters('x') == {'x': 1})
print(count_letters('') == {})
print(count_letters('!!!') == {})