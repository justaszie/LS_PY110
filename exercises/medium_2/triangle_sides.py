"""
PROBLEM
- Input: 3 float values: length of sides of a triangle
- Output: str - Type of triangle
- Explicit rules:
    - Output value has 4 options:
        - "invalid" if (a) either side is 0 or (b) sum of shorter sides < longest side
        - "equilateral" if all sides have same length
        - "isosceles" if 2 sides are equal but not the 3rd
        - "scalene all 3 sides are equal

- Implicit rules:
    - lengths can be passed as floats or ints

- Questions:
    - Negative input values

ALGORITHM
1. If any side is <= 0, return 'invalid'
2. Sort the inputs by length in ascending order
3. If the sum of the 1st and 2nd input is less or equal to the 3rd input, return 'invalid'
4. If all 3 inputs are equal, return 'equilateral'
5. if 1st and 2nd argument are equal OR 2nd and 3rd argument are equal OR 1st and 3rd argument are equal:
    - return 'isosceles'
6. return 'scalene'

IMPLEM NOTES
-

"""

def triangle(side1, side2, side3):
    sides = [side1, side2, side3]

    if any([side <= 0 for side in sides]):
        return 'invalid'

    sides.sort()
    if sides[0] + sides[1] <= sides[2]:
        return 'invalid'

    if side1 == side2 == side3:
        return 'equilateral'

    if side1 == side2 or side2 == side3 or side1 == side3:
        return 'isosceles'

    return 'scalene'


print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True