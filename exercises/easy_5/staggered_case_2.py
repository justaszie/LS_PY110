"""
PROBLEM
- Input: string
- Output: string with staggered case
- Explicit Rules:
    - Every other character, starting from first, must be capitalized.
    - The non-alphabetic characters do not count when determining the character to capitalize.
        E.g. 'my house' => 'My HoUsE' 
    - Non-alphabetic characters are still added to the result string
- Implicit Rules:
- Questions: 

EXAMPLES

DATA STRUCTURES

ALGORITHM
1. Set alphabetic characters counter to 0 
Create an empty result string
2. Iterate over the index values of the input string (0 to string length - 1 incl.). For each value:
    A. If the current character is alphabetic:
        (i) If the alpha char counter is pair:
            - Append the capitalized version of the current char to the result string
        (ii) Else:
            - Append the lowercase version of the current char to the result string
        (ii) Increment the alphabetic character counter by 1 
    B. Else:
        - Append the current character to the result string 

IMPLEM NOTES
- alpha_char_counter
"""

import pdb

def staggered_case(string):
    # V1 
    result = ''
    alpha_chars_counter = 0

    for idx, char in enumerate(string):
        if char.isalpha():
            result += char.capitalize() if alpha_chars_counter % 2 == 0 else char.casefold()
            alpha_chars_counter += 1
        else:
            result += char
    
    return result


print(staggered_case("I Love Launch School!") == "I lOvE lAuNcH sChOoL!")
pdb.set_trace()
print(staggered_case("ALL CAPS") == "AlL cApS")
print(staggered_case("ignore 77 the 444 numbers") == "IgNoRe 77 ThE 444 nUmBeRs")
print(staggered_case('my house') == 'My HoUsE')