"""
PROBLEM
- Input: a string
- Output: string with number-words converted to digit form
- Explicit Rules:
    - Number words: one, two,...., nine will be converted to digit form: 1, 2,..9
    - String doesn't contain any punctuation. I.e. there will be no substrings such as 'nine,' or 'ninety-nine' 
- Implicit Rules: 
    - 
- Questions:
    - Assuming that if input is empty string, output is also empty string
    - Edge cases - composite numbers with no punctuation. Examples:  'ninety nine' will become 'ninety 9', 'one hundred and 4' will be '1 hundred and 4'. 

EXAMPLES
message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True

DATA STRUCTURES 
Strings 


ALGORITHMS 
1. Create a dictionary mapping words to their digit representation.
2. Create a copy of the input string "result"
3. Iterate over the keys inside the mapping dictionary. For each key:
    - If the key is found in the "result" string, replace the word with the associated digit (value)
    - Reassign the result to the new string with replaced number word
4. Return result value

IMPLEM NOTES

FURTHER EXPLORATION 
Consider that the words can end with punctuation. E.g. three, four.


1. Iterate over each word in the message.
2. Strip punctuation from the word 
3. Replace the word with the mapped value, if the word is in the mapping 

"""

def word_to_digit(message):
    mapping = {
        'zero' : '0',
        'one': '1',
        'two': '2', 
        'three':'3', 
        'four': '4', 
        'five': '5', 
        'six': '6', 
        'seven': '7', 
        'eight': '8', 
        'nine': '9'
    }

    # words_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'] 

    for word in mapping:
        message = message.replace(word, mapping[word])

    # message_words = message.split()
    # for idx,mw in enumerate(message_words):
    #     if mw in words_list:
    #         message_words[idx] = str(words_list.index(mw))

    # return ' '.join(message_words)

    return message

import string 

def strip_punctuation(word):
    punct = [char for char in word if char in string.punctuation] 
    stripped_word = ''.join([char for char in word if char not in string.punctuation])
    return stripped_word, punct

def word_to_digit_fe(message):
    mapping = {
        'zero' : '0',
        'one': '1',
        'two': '2', 
        'three':'3', 
        'four': '4', 
        'five': '5', 
        'six': '6', 
        'seven': '7', 
        'eight': '8', 
        'nine': '9'
    }

    words = message.split()
    new_words = [] 
    for word in words:
        word_without_punct, punct_list = strip_punctuation(word)
        if word_without_punct in mapping:
            new_word = mapping[word_without_punct]
            for punct in punct_list:
                new_word += punct
        else:
            new_word = word
        
        new_words.append(new_word)

    return ' '.join(new_words)


    # return ' '.join([mapping.get(strip_punctuation, ) for word in words])
    # for word in words:
    #     word = strip_punctuation(word)


message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True

message = 'Please call me at five, five, five, one, two, three, four.'
print(word_to_digit(message))
print(word_to_digit(message) == "Please call me at 5, 5, 5, 1, 2, 3, 4.")
# Should print True
