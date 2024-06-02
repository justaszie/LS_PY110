"""
PROBLEM 
- Input: dictionary
- Output: list containing the input dictionary keys, sorted based on their values
- Explicit Rules:
    - Create a list of keys from the input dictionary, sort it by their respective value and return it
- Implicit Rules:
    - Sorting in ascending order
    - Assumption: sorting will always be done based on numeric comparison (either comparing numbers or numeric Unicode values of strings)
    - Assumption: output for empty dictionary will be empty list
- Questions:
    - What values are possible 

EXAMPLES
print(order_by_value({'p': 8, 'q': 2, 'r': 6}))
# ['q', 'r', 'p']

DATA STRUCTURES

ALGORITHM
1. Get the list of keys
2. Sort the list based on the associated values in ascending order

IMPLEM NOTES
- may use get method as key for sorting 

"""
def order_by_value(dictionary):
    keys = list(dictionary.keys())
    keys.sort(key=dictionary.get)
    # return keys
    return sorted(list(dictionary.keys()), key=dictionary.get)


print(order_by_value({'p': 8, 'q': 2, 'r': 6}))
# ['q', 'r', 'p']

print(order_by_value({}))
# []

