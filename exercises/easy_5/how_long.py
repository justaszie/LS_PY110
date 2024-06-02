"""
PROBLEM
- Input: a string
- Output: a list 
- Explicit Rules:
    - Output list should contain:
        - (1) every word from the input string, 
        - (2) followed by a space 
        - (3) and the word's length
    - If the input is Empty string or no argument is passed, output should be empty list
- Implicit Rules:
    - Format of output list elements: '{word} {word length}'
    - Apostrophe and punctuation is included in the word
    - Assuming that separation of words is based on a whitespace character. Any other character (e.g. hyphen, punctuation, digits, special characters) is included in the word count
    - If there are no spaces, the output will have 1 word
- Questions: 
    - Definition of word (punctuations)
    - Word length count to include all special chars and digits? 
    - Only one word 

EXAMPLES
print(word_lengths('cow sheep chicken'))
# ['cow 3', 'sheep 5', 'chicken 7']

print(word_lengths('baseball hot dogs and apple pie'))
# ['baseball 8', 'hot 3', 'dogs 4', 'and 3', 'apple 5', 'pie 3']

print(word_lengths("It ain't easy, is it?"))
# ['It 2', "ain't 5", 'easy, 5', 'is 2', 'it? 3']

print(word_lengths('Supercalifragilisticexpialidocious'))
# ['Supercalifragilisticexpialidocious 34']

print(word_lengths(''))      # []
print(word_lengths())        # []

print(word_lengths("She's a man-eater")) # ["'She's' 5", 'a 1', 'man-eater 9']

DATA STRUCTURES
Strings, lists 

ALGORITHM
0. Create an empty result list
1. If no input provided or if the input is an empty string:
    - Return the empty result list
2. Split the input string into a words list
3. Iterate over the words list. For each value:
    A. Calculate the word length
    B. Create a new string with the required format '{string} {length}'
    C. Add the new string to the end of the result list.

IMPLEM NOTES
- How to specify an optional parameter in a function? Is it the last position in the parameters list?
- Return value of str.split() with only 1 word ? 
"""

def word_lengths(string=None):
    # v1 
    # result = []
    
    # if not string:
    #     return result
    
    
    # words = string.split()

    # for word in words:
    #     result.append(f"{word} {len(word)}")

    # return result 

    # v2 - comprehension
    return [f"{word} {len(word)}" for word in string.split()] if string else []

print(word_lengths('cow sheep chicken'))
# ['cow 3', 'sheep 5', 'chicken 7']

print(word_lengths('baseball hot dogs and apple pie'))
# ['baseball 8', 'hot 3', 'dogs 4', 'and 3', 'apple 5', 'pie 3']

print(word_lengths("It ain't easy, is it?"))
# ['It 2', "ain't 5", 'easy, 5', 'is 2', 'it? 3']

print(word_lengths('Supercalifragilisticexpialidocious'))
# ['Supercalifragilisticexpialidocious 34']

print(word_lengths(''))      # []
print(word_lengths())        # []

print(word_lengths("She's a man-eater")) # ["'She's' 5", 'a 1', 'man-eater 9']