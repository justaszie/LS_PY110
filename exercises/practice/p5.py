"""
PROBLEM
- Input: string
- Output: most frequent character
- Rules:
    - If multiple characters, return the one that occurs first
    - Counting is case insensitive. C and c both count same
- Questions:
    - If we have C and c, which should be returned? Assuming the lower case always.
    - Should we count whitespace characters?
    - What should we return for empty string?


DATA STRUCTURES
1. Dict for character: frequency pairs
2. Sorting the dict keys based on the value

ALGORITHM
1. Count frequency of all characters (case insensitive)
    - Iterate over the string and add / increment dictionary
2. Find the highest frequency manually
    - assign the maximum value and minimum key variables
    - iterate over the rest of the keys and reassign the maximum values if higher value is found



"""

def most_common_char(string):
    counts = {}
    for char in string:
        counts.setdefault(char.casefold(), 0)
        counts[char.casefold()] += 1

    sorted_keys = sorted(list(counts.keys()), key=counts.get, reverse=True)
    return sorted_keys[0]

    chars = list(counts.keys())

    max_char = chars[0]
    max_value = counts[max_char]

    for char in chars[1:]:
        if counts[char] > max_value:
            max_value = counts[char]
            max_char = char

    return max_char

print(most_common_char('Hello World') == 'l')
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')

my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p')

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')

my_str = 'EeAa'
print(most_common_char(my_str))