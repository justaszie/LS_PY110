"""
PROBLEM
- Input: string
- Output: int - greatest product of 4 consecutive digits
- Rules:
    - Input will always have >= 4 digits and will only contains digits
- Questions:

ALGORITHM
[*] 1. Collect all combinations of 4 consecutive digits
[**] 2. Find the maximum integer value among the combinations.


[*]
Iterate from 0 to len(input string) - 3 (excl)
    On each iteration, take a slice of the string [start:start+4]. Add it to the list of combinations.


[**]
Iterate over the combinations and calculate the product of its digits, store in a list
Return maximum from the list


[0][1][2][3]
1   2  3  4

last index = 3
lenght = 4
first index = 0

Interval from 0 to 1 (excl)

[0][1][2][3][4]
1   2  3  4  5

1-4
2-5

len = 5
last index = 4
Interval from 0 to 2 (excl)


"""

def digits_product(string):
    product = 1
    for char in string:
        product *= int(char)

    return product

def greatest_product(string):
    # Iterate from 0 to len(input string) - 3 (excl)
    # On each iteration, take a slice of the string [start:start+4].
    combinations = []
    for start in range(len(string) - 3):
        combinations.append(string[start:start + 4])

    products = [ digits_product(combo) for combo in combinations]
    return max(products)


print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6