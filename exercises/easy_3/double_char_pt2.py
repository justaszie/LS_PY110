"""
PROBLEM
- Inputs: string
- Outputs: new string with modified characters from input string
- Explicit Rules:
    - Result string contains the characters from the input string in the original order but:
        - every consonant from the input string is doubled
        - adding the vowels, digits, special characters and whitespaces from the input string once
- Implicit Rules:
    - Empty string returns empty string 
    - Assuming case is important
- Questions:
    - Is case important? (from examples it seems so, but want to confirm)

EXAMPLES
# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")

DATA STRUCTURES
Strings 
Lists

ALGORITHM
0. Create an empty result string 
1. Loop through the characters of a string.
2. If the character is a consonant:
    - Create a substring by doubling the character
    - Append the substring to the result string
3. Else:
    - Append the character to the result string 
4. Return the result string 

(2) DETAIL:
1. If the character is one of the following: 
    ('b',
'c',
'd',
'f',
'g',
'h',
'j',
'k',
'l',
'm',
'n',
'p',
'q',
'r',
's',
't',
'v',
'w',
'z',
'x',
'y')
    - return True
2. Else:
    return False 



IMPLEM NOTES
- Use comprehension and converting to strings 
- Checking against consontant may not be efficient. Think of better logic condition 

"""

def is_consonant(char):
    char = char.lower()
    return char.isalpha() and char not in ('a','e','i','o','u')
 

def double_consonants(string):
    return ''.join(
        [char * 2 if is_consonant(char) else char for char in string]
    )


# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")