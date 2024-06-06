def sum(numbers, factor):
    total = 0
    for n in numbers:
        total += n
    return factor * total

numbers = [1, 2, 3, 4]
print(sum(numbers, 2) == 20)

# Multiply the sum by the factor 
# Our created sum function shadows the built-in sum function. So on line 2 we are calling our defined sum function without providing all the arguments.
# Solution 1: rename our function to "custom_sum"
# Solution 2: don't use built in sum