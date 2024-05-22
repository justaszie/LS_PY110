"""
Modify the word_sizes function from the previous exercise 
to exclude non-letters when determining word size. 
For instance, the word size of "it's" is 3, not 4.

0. Create an empty result dictionary
1. Get all the words from input string. Words = substrings separated by space.
2. Iterate over the list of words. For each word:
    A. Calculate the length. 
        - Exclude the non-alphabetic characters when counting the word length
        - Set length to 0  
        - Iterate over each character:
            - If the character is alphabetic, increment length 
        - return the length 
    B. If the length is present in the resulting dictionary:
            - Increment the count of words for that length by 1 
        Else, 
            - Add 1 as the word count for that lenght 
3. Return the result dictionary

Detailed Algorithm - get word lenght
1. Set length to 0  
2. Iterate over each character:
    A. If the character is alphabetic, increment length 
3. return the length 

""" 
def get_word_length(word):
    length = len([char for char in word if char.isalpha()])
    
    return length 

def word_sizes(text):
    result = {}
    words_list = text.split()

    for word in words_list:
        length = get_word_length(word)
        # One edge case are words that are 0 lenght, when excluded non-alphabetic characters
        if length:
            result[length] = result.get(length, 0) + 1
    
    return result 

# All of these examples should print True

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

string = "What's ''' ''' up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})