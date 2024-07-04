"""
PROBLEM
- Input: string
- Output: tuple (str, int)
- Rules:
    - Input string will never be empty and is only composed of lowercase alphabetic letters
    - Output:
        - {str} is shortest possible substring
        - {int} is the largest possible repeat count.
        - the input string can be completed by repeating the {str} a number of times {int}
        - If the string can't be completed through repetition, the output is just same string, repeated 1 time.
- Questions


ALGORITHM
1. Collect all substrings
2. Sort the substrings by length
3. For each substring, iterate over X int values while substr * X is shorter than input string.
    - If match is found, where substring * x == input string, break out of the loop. Return the tuple of subs, x


1 - collect substrings:
    - Iterate over start indexes (0 to len(string) excl)
        - Iterate over end indexes (start + 1 to len(string), incl)
            take the substrings, add to the list

2 - sorting
    - sort substrings list by length

3 - finding a match:
    - Iterate over substrings list. On each iteration
        - set x to 0
        - Iterate while len(substring * x) < len (input string). On each iteration
            increment x by 1
            if substring * x == input string: quit both loops and return the tuple value with substring and x

IMPLEM NOTES
- If nested loops don't work, try while True with return and break keywords.



"""
def get_substrings(string):
    substrings = []
    for start in range(len(string)):
        for end in range(start + 1, (len(string) + 1)):
            substrings.append(string[start:end])

    return substrings

def repeated_substring(str):
    substrings = get_substrings(str)

    substrings.sort(key=len)

    for sub in substrings:
        x = 1
        # When it's equal, the loop will still run once and return the value.
        # We only quit the loop once we went over the input string lenght
        while (len(sub * x) <= len(substrings)):
            if sub * x == str:
                return (sub, x)
            x += 1

        # Alternative with while True
        # x = 1
        # while True:
        #     if sub * x == string:
        #         return (sub, x)
        #     if len(sub * x) > len(string):
        #         break
        #     x += 1

print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))