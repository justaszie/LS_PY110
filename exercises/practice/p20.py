"""
PROBLEM
- Input: list of numbers (1 number is not the same as others)
- Output: the number that is not same as others
- Rules:
    - The list will always contain at least 3 numbers and exactly 1 number that will be different tha nothers
- Questions:


ALGORITHM
1. Count the occurences of each number
2. Return the number that occurs only once.

"""

def what_is_different(numbers):
    counts = { }
    for number in numbers:
        counts[number] = counts.get(number, 0) + 1

    for number, count in counts.items():
        if count == 1:
            return number

print(what_is_different([0, 1, 0]) == 1)
print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
print(what_is_different([3, 4, 4, 4]) == 3)
print(what_is_different([4, 4, 4, 3]) == 3)