"""
PROBLEM
- Input: list of integers
- Output: MINIMUM integer to append so that sum of list = closest prime number greater than the current sum
- Rules:
    - S = current sum of integers in the list
    - Append x to the list. Sum with x = Z. Z == closest prime number greater than S
        (1) Find the prime number closest to S = Y
        (2) Iterate over integer values and find the number that makes the new sum == Y
    - List always contains >= 2 numbers
    - All values are positive
    - May be multiple occurences of numbers in the list (don't worry about adding duplicate number)
    -
- Questions:
    - What is a prime number?  => number that can only be divided by itself and 1.


ALGORITHM
1. Find the nearest prime number greater than the sum of input integers:
    - Calculate the sum of the integers S
    - Iterate over integer values starting from S+1 until we find a prime number
        - Iterate until prime number found.
            - Set iterator to S + 1
            - Check if S + 1 is prime (* function is prime)
            - If yes, stop and assign the current iterator value to closest_prime
            - If not, continue with S + 2 and repeat.

2. Set min integer value to 1
3. Iterate until sum of input list numbers == closest prime number. On each iteration:
    A. create new list that concatenates input list and the min integer value.
    B. If the sum of the new list members == prime number:
        - return the min integer value
    C. Else, increment min integer value by 1 and continue



"""
def is_prime(number):
    # [2 - number - 1]. No X where number % x == 0
    if number < 2:
        return False
    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    return True


def closest_prime_number(numbers_list):
    numbers_sum = sum(numbers_list)
    min_int = numbers_sum + 1
    while True:
        if is_prime(min_int):
            return min_int
        else:
            min_int += 1

def nearest_prime_sum(numbers_list):
    nearest_prime_num = closest_prime_number(numbers_list)
    min_integer = 1
    while True:
        new_list = numbers_list + [min_integer]
        if sum(new_list) == nearest_prime_num:
            return min_integer
        else:
            min_integer += 1


print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)