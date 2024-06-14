""" 
PROBLEM
- Input: positive integer as an argument
- Output: true / false specifying if the number is prime or not 
- Explicit Rules:
    - prime number is a positive number that is evenly divisible only by itself and 1
    - Number 1 is NOT prime
- Implicit Rules:
- Questions:
    - Assuming no input validation is needed
    - 

EXAMPLES
- provided 

DATA STRUCTURES
- lists for all divisors 

ALGORITHM

1. If number is 1, return False
2. Else, continue
3. Create an empty divisors list
3. Iterate over numbers from 1 up to the input number, included. 
    if the input number is evenly divisible by the current iteration value:
        - Add the current iteration value to the list of divisors
4. If the divisors list has > 2 elements, return False
5. Else, return True 

IMPLEM NOTES

"""
def is_prime(number):
    if number == 1:
        return False
    
    divisors = [1]

    for divisor in range (2, number + 1):
        if number % divisor == 0:
            divisors.append(divisor)
    
    return len(divisors) <= 2


print(is_prime(1) == False)              # True
print(is_prime(2) == True)               # True
print(is_prime(3) == True)               # True
print(is_prime(4) == False)              # True
print(is_prime(5) == True)               # True
print(is_prime(6) == False)              # True
print(is_prime(7) == True)               # True
print(is_prime(8) == False)              # True
print(is_prime(9) == False)              # True
print(is_prime(10) == False)             # True
print(is_prime(23) == True)              # True
print(is_prime(24) == False)             # True
print(is_prime(997) == True)             # True
print(is_prime(998) == False)            # True
print(is_prime(3_297_061) == True)       # True
print(is_prime(23_297_061) == False)     # True