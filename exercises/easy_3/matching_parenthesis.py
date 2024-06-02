"""
PROBLEM
- Input: string
- Output: boolean
- Explicit Rules:
    - Output is True if the string has balanced parentheses
    - Balanced parentheses = occurring in matching pairs ( and ). I.e. Every 
    opening parenthesis must be closed before the string ends. Every closing parenthesis must occur after an opening one. 
- Implicit Rules:
    - string with no parentheses should return True as if they were balanced
    - Assumption: input will not be empty string
- Questions: 
    - Can the input be empty string?



EXAMPLES

print(is_balanced("What (is) this?") == True)
# Closing with no opening 
print(is_balanced("What is) this?") == False)
# Opening with no closing 
print(is_balanced("What (is this?") == False)
print(is_balanced("((What) (is this))?") == True)
print(is_balanced("((What)) (is this))?") == False)
print(is_balanced("Hey!") == True)
# Closing with no opening prior and opening with no closing
print(is_balanced(")Hey!(") == False)
print(is_balanced("What ((is))) up(") == False)

DATA STRUCTURES
Example: "What ((is))) up(" 

After parsing 2 opening p.
[
{'start_position': 5, state:'open'
},
{'start_position': 6, state:'open'}
]

ALGORITHM
1. Go through the string characters one by one. For each character:
    A. If an opening parenthesis is found:
        - Append the character to the list of open parentheses
    B. If a closing parenthesis is found:
        - If there is at least one parenthesis in opened state:
            - Remove a random eleemnt from the list of open parenthesis
        - Else:
            - Stop and return False because there's an closing before opening
2. If there are parentheses in opened state:
    - Return False because there was an opening that was not closed
3. Else:
    - Return True. 

"""

# def is_balanced(string):
#     open_parentheses = []

#     for char in string:
#         if char == '(':
#             open_parentheses.append(char)
#         elif char == ')':
#             if open_parentheses:
#                 open_parentheses.pop()
#             else:
#                 return False
                
#     return not open_parentheses


# print(is_balanced("What (is) this?") == True)
# print(is_balanced("What is) this?") == False)
# print(is_balanced("What (is this?") == False)
# print(is_balanced("((What) (is this))?") == True)
# print(is_balanced("((What)) (is this))?") == False)
# print(is_balanced("Hey!") == True)
# print(is_balanced(")Hey!(") == False)
# print(is_balanced("What ((is))) up(") == False)


"""
FURTHER EXPLORATION

(), [] , {}, '', "" <-- These all should also come in pairs

ALGORITHM
1. Go through the string characters one by one. For each character:
    A. If an opening parenthesis, square bracket, curly brace is found:
        - Append the character to the list of opening characters
    B. If a closing parenthesis, square bracket, curly brace is found:
        - If there is at least one character in opening characters that is closing parenthesis, square bracket or curly brace (depending on current character):
            - Remove that eleemnt from the list of open parenthesis
        - Else:
            - Stop and return False because there's an closing before opening
    C. If the current character is a single or double quote character:
        - If there is already one signle / double quote char in opening characters:
            - Remove it from the list
        - Else:
            - Add it to the list 
2. If there are any elements in opening characters
    - Return False because there was an opening that was not closed
3. Else:
    - Return True. 

"""

def is_balanced_fe(string):
    opening_characters = []

    closing = {
        ')': '(',
        ']': '[',
        '}': '{',
    }

    for char in string:
        if char in closing.values():
            opening_characters.append(char)
        elif char in closing.keys():
            if closing[char] in opening_characters:
                # If a closing is found, remove 1st occurence of the corresponding opening 
                opening_characters.remove(closing[char])
            else:
                return False # A closing is found before an opening
        # If encountered a single / double quote and it's already opened, remove it. 
        # Otherwise, keep track of an opening
        elif char in ["'", '"']:
            if char not in opening_characters:
                opening_characters.append(char)
            else:
                opening_characters.remove(char)
    
    # Return True if there are no opening characters without closing 
    return not opening_characters


print(is_balanced_fe("What [is] this?") == True)
print(is_balanced_fe("What is} this?") == False)
print(is_balanced_fe("What {is this?") == False)
print(is_balanced_fe("({What} (is this))?") == True)
print(is_balanced_fe("((What)) (is this))?") == False)
print(is_balanced_fe("Hey!") == True)
print(is_balanced_fe(")Hey!(") == False)
print(is_balanced_fe("What ({is]}) up(") == False)