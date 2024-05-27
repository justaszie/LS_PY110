"""
PROBLEM
- Inputs: string
- Outputs: New string with each character of initial string doubled
- Explicit Rules:
    - Return new string that has each character of input string doubled
- Implicit Rules:
    - Assuming case is important 
    - Assuming spaces and other special characters are doubled too 
    - Empty string returns an empty string
    - Assuming no input validation is required
- Questions: 
    - Case is important? ie.. 'C' needs to be doubled with 'C' and 'c' with another 'c' 
    - Should spaces be doubled too? (it looks like it from the example but not sure)
    - Input validation not required? 

EXAMPLES 
print(repeater('Hello'))        # "HHeelllloo"
print(repeater('Good job!'))    # "GGoooodd  jjoobb!!"
print(repeater(''))             # ""

DATA STRUCTURES
Strings

ALGORITHM:
1. Create an empty string "result"
2. Loop through all characters of the input string. For each character
    A. Create a substring that is composed of the current character twice
    B. Append the substring to the result string
3. Return result string 
"""

def repeater(string):
    result = ''
    
    for char in string:
        result += char * 2

    return result


print(repeater('Hello') == "HHeelllloo")        # "HHeelllloo"
print(repeater('Good job!') == "GGoooodd  jjoobb!!")    # "GGoooodd  jjoobb!!"
print(repeater('') == "")             # ""
print(repeater(' ') == "  ")    