"""
PROBLEM
- Input: dictionary with unique keys and unique associated values
- Output: dictionary where input dictionary keys are values and input dictionary values are keys
- Explicit Rules: defined in output
- Implicit Rules:
    - Assuming that input dictionary values will be hashable 
    - The values inside the input dictionary are unique which allows them to be used as keys
    - Assuming empty dictionary will return an empty dictionary 
- Questions
    - input dictionary values must be hashable type to be used as keys.

EXAMPLES
print(invert_dict({'apple': 'fruit', 'broccoli': 'vegetable', 'salmon': 'fish'}))
# {'fruit': 'apple', 'vegetable': 'broccoli', 'fish': 'salmon'}


DATA STRUCTURES
Dict

ALGORITHMS
1. Create an empty dictionary "result"
2. Iterate through the key-value pairs of the input dicitonary. For each iteration:
    A. Create a key-value pair in the "result" dictionary where the key from current iteration is used as value of the new pair, and value from current iteration is used as key of the new pair.
3. Return the result dictionary 

IMPLEM NOTES
using .items() to iterate over key value pairs
"""

def invert_dict(dictionary):
    # result = {}
    # for key, value in dictionary.items():
    #     result[value] = key 

    # return result

    # V2 
    return {input_value: input_key for input_key, input_value in dictionary.items()}


print(invert_dict({'apple': 'fruit', 'broccoli': 'vegetable', 'salmon': 'fish'}))
# {'fruit': 'apple', 'vegetable': 'broccoli', 'fish': 'salmon'}