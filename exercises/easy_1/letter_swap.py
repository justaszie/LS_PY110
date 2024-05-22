"""
Given a string of words separated by spaces, write a function that swaps the first and last letters of every word.

You may assume that every word contains at least one letter, and that the string will always contain at least one word. You may also assume that each string contains nothing but words and spaces, and that there are no leading, trailing, or repeated spaces.

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True


PROBLEM 
- Inputs: string of words
- Outputs: string of words with first and last letters of every word swapped
- Explicit Rules:
    - For each word, the first and last letters are swapped
    - Words are separated by spaces
    - Every word contains at least one letter. 
    - There is at least one word in the string. Minimum string will be at least one letter 'a' 
    - There are only words and spaces in the string.
        - No leading, trailing, repeated spaces
        - No special characters
- Implicit Rules:
    - For words of one letter, the output word will be same as input
    - Assuming that the words only include alphabetic characters
    - Letter case is important when swapping.
    - Assuming that we can return a new object, not modifying the input. 


EXAMPLES
print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True

3. Data Structures
- Strings

ALGORITHM
1. Get a list of words contained in the string
2. Create an empty list of swapped words
3. Loop over the list of words. For each word:
    A. If the word is at least 2 characters
            - Create a result string that is a concatenation of: (1) last character of word  + (2) word characters from 2nd to the next to the last character + (3) the first character of the word
        Else,
            - assign the word value to the result string 
    B. Append the result to the swapped words list 
4. Convert the list of swapped words to a result string
5. Return the result string



"""

def swap(string):
    words_list = string.split()
    swapped_words_list = []

    for word in words_list:
        if len(word) > 1 :
            result = word[-1] + word[1:-1] + word[0]
        # print(result)
        else:
            result = word

        swapped_words_list.append(result)

    # print(' '.join(swapped_words_list))
    return ' '.join(swapped_words_list)
    


print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True