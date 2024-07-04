"""
PROBLEM
- Input: list of integers
- Output: integer that appeasr an odd number of times
- Rules: there will always be only one integer that appears odd number of times
-
- Questions

ALGORITHM
1. Count the occurences of each number
    - Iterate over list and increment counts dictionary
2. Iterate over the items in counts dictionary and return the key that has an odd number of counts

"""
def odd_fellow(numbers_list):
    counts = {}
    for number in numbers_list:
        counts[number] = counts.get(number, 0) + 1

    for number, count in counts.items():
        if count % 2 == 1:
            return number

print(odd_fellow([4]) == 4)
print(odd_fellow([7, 99, 7, 51, 99]) == 51)
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
print(odd_fellow([0, 0, 0]) == 0)