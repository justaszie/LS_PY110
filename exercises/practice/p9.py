"""
PROBLEM
- Input: 2 strings
- Output: number of times the 2nd string occurs in the 1st string
- Rules:
    - Overlapping occurences don't count ('bab' occurs once in 'babab'). Count only distinct occurences.
    - 2nd argumnt is never an empty string
    - If 1st argument is empty string, return 0
- Questions:
    - Assuming the matching should be case sensitive.

ALGORITHM
[*] 1. Get all substrings from input string.
2. Count the number of substrings that match exactly the 2nd argument

[*]
babab

start 0 -> [-1]
    end start + 1 -> [len]
str[start:end]

0  01  012  0123  01234
b, ba, bab, baba, babab

1  12  123  1234
a, ab, aba, abab
...

0. Set count of occurences to 0
1. Iterate over indices from 0 to len-1. Assign to start variable. On each iteration:
    Iterate over indices from start + 1 to len (included). Assign to end variable. On each iteration:
        Take a slice of the string starting from start, ending with end (excl.)
        if the slice equals exactly the 2nd argument:
            - Increment the count of occurences
2. Return the count of occurences

"""

def count_substrings(string, sub):
    if not string:
        return 0

    count = 0

    for start in range(len(string)):
        for end in range(start + 1, len(string) + 1):
            slice = string[start:end]
            if slice == sub:
                count += 1

    return count

    # return string.count(sub)


print(count_substrings('babab', 'bab') == 1)
print(count_substrings('babab', 'ba') == 2)
print(count_substrings('babab', 'b') == 3)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('', 'x') == 0)
print(count_substrings('bbbaabbbbaab', 'baab') == 2)
print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)