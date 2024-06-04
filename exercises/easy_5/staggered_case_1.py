"""
PROBLEM
- Input: string
- Output: string that represents input string with staggered capitalization
- Explicit Rules:
    - Staggered capitalization: 
        - Startign from 1st character, every other character needs to be capitalized. 
        - non-alphabetic characters are not changed but they are counted to decide which character needs to be capitalized.
- Implicit Rules:
    - spaces are also counted when deciding which character to capitalize. E.g. 'my house' => 'My hOuSe'
- Questions: 
    - Assuming empty string returns empty string
    - Assuming 1 character string returns the string with that character capitalized

EXAMPLES
-  'my house' => 'My hOuSe'

DATA STRUCTURES
- strings

ALGORITHM
1. Create an empty "result" string
2. Iterate over the index values from 0 up to the length of input string, exclusive. For each index value:
    - If the index is a pair number:
        - If the character at the current index is alphabetic:
            - Capitalize the character at the current index and append it to result string
        - Else:
            - append the character at the current index to the result string
    - Else:
        - If the character at the current index is alphabetic:
            - Convert the character to lower case and append it to the result string
        - Else:
            - append the character at the current index to the result string


IMPLEM NOTES
"""

# V1 
# def get_correct_character(string, index):
#     current_char = string[index]

#     if index % 2 == 0:
#             return current_char.capitalize() if current_char.isalpha() else current_char
#     else:
#             return current_char.casefold() if current_char.isalpha() else current_char

# def staggered_case(string):
#     # V1
#     result = ''
#     for idx in range(len(string)):
#         result += get_correct_character(string, idx)
    
#     return result

# V2
# def staggered_case(string):
#     # One issue is that we're doing capitalize/casefold on special characters. Not sure it's good
#     chars = [string[idx].capitalize() if idx % 2 == 0 else string[idx].casefold() for idx in range(len(string))]
#     return ''.join(chars)

# V3
def get_correct_character(string, index):
    current_char = string[index]

    if index % 2 == 0:
            return current_char.capitalize() if current_char.isalpha() else current_char
    else:
            return current_char.casefold() if current_char.isalpha() else current_char

def staggered_case(string):
    return ''.join([get_correct_character(string, idx) for idx in range(len(string))])


print(staggered_case('I Love Launch School!'))        # "I LoVe lAuNcH ScHoOl!"
print(staggered_case('ALL_CAPS'))                     # "AlL_CaPs"
print(staggered_case('ignore 77 the 4444 numbers'))   # "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case('my House'))   # "My hOuSe