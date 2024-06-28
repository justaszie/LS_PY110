"""
PROBLEM
- Input: integer
- Output: integer (nth number in Fibonacci sequence)
- Explicit Rules:
    - fib seris = numbers sequence. 
        - 1st and 2nd numbers are 1 
        - Then: n = n-2 + n-1
    - Calculate F(n) - i.e. n-th number in fibonacci sequence
- Questions:
    - Assuming no input validation is needed. n will always be > 0

Input | Series
1       1 
2       11
3       112




ALGORITHM
1. If n < 2: return 1
2. Initialize the fibonacci list to [1, 1]
3. Iterate over a range of integers starting from 2 to N-1 (input) value, included. For each iteration:
    A. Calculate the x-th sequence number (where x is current iterator value). Use formula (x-2 + x-1)
    B. Append the calculated x-th sequence number to the fibonacci list
4. return the last element in fibonacci list

Input: 3
List = [1, 1]
Iterate 2 - 2:
    value = 1 + 1 = 2 
    a 


IMPLEM NOTES

"""


def fibonacci(n):
    if n <= 2:
        return 1
    sequence = [1, 1]

    for iterator in range(2, n):
        value = sequence[iterator - 2] + sequence[iterator - 1]
        sequence.append(value)

    return sequence[-1]


print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True
