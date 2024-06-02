"""
PROBLEM
- Inputs: 
    - A dictionary
    - A list of keys
- Output:
    - A new dictionary that only has the keys specified in 2nd argument
- Explicit Rules
    - The return value is a new object
    - The return object has the key-value pairs of the input dictionary but only for the keys specified as the 2nd argument
- Implicit Rules
    - Assuming no input validation is required. E.g. list will contain elements of the same data type as the dict keys.
    - Assuming that empty dictionary leads to returning empty dicitonary
    - Assuming empty list leads to returning empty dictionary
- Questions
    - 

EXAMPLES
# 1
print(keep_keys({'red': 1, 'green': 2, 'blue': 3, 'yellow': 4}, ['red', 'blue']))
# {'red': 1, 'blue': 3}

# 2 
print(keep_keys({}, ['red', 'blue']))
# {}

# 3
print(keep_keys({'red': 1, 'green': 2, 'blue': 3, 'yellow': 4}, ['baadcc']))
# {}

# 3
print(keep_keys({'red': 1, 'green': 2, 'blue': 3, 'yellow': 4}, []))
# {}

DATA STRUCTURES
Dict, list

ALGORITHM
1. Create an empty result dictionary
2. Iterate over each key-value pair of input dictionary. For each iteration
    A. If the current key value appears in the input list of keys:
        - Add the current key-value pair to the result dictionary
3. Return the result dictionary 


IMPLEM NOTES
- Dict comprehension with a selection criteria 
- .items() to iterate over k-v pairs
"""

def keep_keys(dictionary, keys_to_keep):
    return {k: v for k, v in dictionary.items() if k in keys_to_keep}

# 1
print(keep_keys({'red': 1, 'green': 2, 'blue': 3, 'yellow': 4}, ['red', 'blue']))
# {'red': 1, 'blue': 3}

# 2 
print(keep_keys({}, ['red', 'blue']))
# {}

# 3
print(keep_keys({'red': 1, 'green': 2, 'blue': 3, 'yellow': 4}, ['baadcc']))
# {}

# 3
print(keep_keys({'red': 1, 'green': 2, 'blue': 3, 'yellow': 4}, []))
# {}