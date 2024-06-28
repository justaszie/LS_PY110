"""
PROBLEM
- Input: year (int)
- Output: number of Friday 13th in that year (int)
- Rules:
    - input year will be > 1752
    - same calendar will remain in the future
- Questions:

ALGORITHM
Iterate over all 13ths of that year and check if it falls on friday

0. Set total unlucky days counter to 0
1. Iterate over all months of the input year. For each iteration
    [!] A. Check if the 13th of that month is a Friday or not.
        - If yes, increment the unlucky days counter
2. Return the unlucky days counter.

[!]
- Given the date (month = M, day = 13), is it Friday?
"""
import datetime

def friday_the_13ths(year):
    unlucky_counter = 0

    for month in range(1, 13):
        date_to_check = datetime.date(year = year, month = month, day = 13)
        if date_to_check.weekday() == 4: # Monday returns 0
            unlucky_counter += 1

    return unlucky_counter

print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True