"""
string consisting of zero or more space-separated words

PROBLEM
- Input: string with 0 or more words, separated by space
- Output: dictionary that maps the word length (key) to number of words of that length (value)
- Explicit rules: 
- Implicit rules:
    - Since there can be 0 words, empty string input is possible
    - Based on examples, we consider any characters in the word to count towards the lenght of the string. No character removal is necessary.
    - Empty string in input results in empty dictionary

- Questions:
    - How do we define a word? Are numbers and special characters allowed in words?
        - Assuming that any characters count towards the length
        - anything should not count OPEN QUESTION
    - If numbers or special characters are allowed in words, do they count in the word length 
        - Judging by examples, yes - what is allowed in word also counts in the length 


    
EXAMPLES:
# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})

DATA STRUCTURES
- String as input
- List of words as interim 
- Dictionary {word length: words count}

ALGORITHM
0. Create an empty result dictionary
1. Get all the words from input string. Words = substrings separated by space.
2. Iterate over the list of words. For each word:
    A. Calculate the length.
    B. If the length is present in the resulting dictionary:
            - Increment the count of words for that length by 1 
        Else, 
            - Add 1 as the word count for that lenght 
3. Return the result dictionary

"""

def word_sizes(text):
    result = {}
    words_list = text.split()

    for word in words_list:
        length = len(word)
        result[length] = result.get(length, 0) + 1
    
    return result 

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})