"""
PROBLEM
- Input: 3 integer values - 3 degrees of angles of a triangle
- Output: string type of triangle
- Rules:
    - Types:
        - Invalid: every any angle is <= 0 OR sum of degrees is not 180
        - Right: one angle is 90 deg
        - Acute: all angles are < 90
        - Obtuse: one angle is > 90
- Questions:




ALGORITHM
1. check if valid. if invalid, return invalid
2. check types

IMPLEM NOTES

"""

def valid_triangle(angle1, angle2, angle3):
    return angle1 > 0 and angle2 > 0 and angle3 > 0 and sum((angle1, angle2, angle3)) == 180

def triangle(angle1, angle2, angle3):
    angles_list = (angle1, angle2, angle3)

    if not valid_triangle(*angles_list):
        return 'invalid'
    elif any([ angle == 90 for angle in angles_list ]):
        return 'right'
    elif all([ angle < 90 for angle in angles_list ]):
        return 'acute'
    else:
        return 'obtuse'


print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True