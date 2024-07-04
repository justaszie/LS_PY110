"""
PROBLEM
- Input: string of digits
- Output: Number of even-numbered substrings
- Rules:
    - Collect substrings which are string representations of numbers. Then, count those that represent even numbers.
    - If the same substring occurs more than once, it counts as multiple substrings
- Questions:
    - Assuming no empty strings

ALGORITHM
General:
Analyze each substring within the string.
If it represents an even number, add to counter

1. Set counter of even substrings to 0.
2. Iterate over indexes from 0 to len(string), excluded. It will be start index of substring. On each iteration:
    Iterate over indexes from start + 1 until len(string), included. It will be the end index of substring. On each iteration
        Assign part of string from {start} to {end} (excl.) to 'substring' variable.
        Convert the substring to an integer
        If the integer value is even (number % 2 == 0), increment the counter of even subs
3. return counter of even substrings
"""

def even_substrings(digits):
    counter = 0
    for start in range(len(digits)):
        for end in range(start + 1, len(digits) + 1):
            sub = digits[start:end]
            if int(sub) % 2 == 0:
                counter += 1
    return counter

print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)