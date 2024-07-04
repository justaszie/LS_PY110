"""
PROBLEM
- Input: integer
- Output: sum of multiples of 7 or 11 that are < input argument
- Rules:
    - If the number is a multiple of both 7 and 11, count just once.
    - If the argument is negative, return 0
    - If the argument is 0, return 0
- Questions:
    -

ALGORITHM
General: Iterate from 1 to the input integer (excl.). Check if the current number is either multiple of 7 or 11. If yes, add it to list
Sum up the numbers in list and return it


"""

def seven_eleven(number):
    if number < 1:
        return 0

    multiples = []
    for x in range(1, number):
        if x % 7 == 0 or x % 11 == 0:
            multiples.append(x)

    return sum(multiples)


print(seven_eleven(10) == 7)
print(seven_eleven(11) == 7)
print(seven_eleven(12) == 18)
print(seven_eleven(25) == 75)
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)