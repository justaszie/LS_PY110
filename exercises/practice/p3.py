"""
PROBLEM
- Input: string
- Output: copy with every 2nd character in every 3rd word coverted to uppercase
- Rules:
    - Words to convert: 3rd, 6th, 9th, etc. (first: 3, then + 3). Idx // 3 == 0 (except )
    - Inside those words, characters to convert: 2, 4, 6...
    - Assuming if str is less than 3 words, return same value
    - Assuming words are separated by any combo of whitespace characters
- Questions:
    - empty string, 1 char
    - How do we define word?

ALGORITHM:
    - Split string into a list of words
    - Iterate over each word, keeping track of the index in the list
    - Considering division of the (index + 1) by 3, if the integer value is >= 1 and remainder is 0:
        [*] - get a copy of the word with every 2nd character replaced
        - Replace the word at the current index with the modified word
    - Join the list of words into a new string with whitespace separator
    - return the new string

[*] Replace characters
    1. Convert the string to a list of characters
    2. Iterate over each character, keeping track of its index in the list:
        A. Considering division of the (index + 1) by 2, if the integer value is >= 1 and remainder is 0:
            - Replace the character at the currend index with the uppercase version of it
    3. Join the characters in the list to a new string with empty string separator
    4. Return the new string


"""
def replace_characters(word):
    chars_list = list(word)

    for idx in range(len(chars_list)):
        if (idx + 1) // 2 >= 1 and (idx + 1) % 2 == 0:
            chars_list[idx] = chars_list[idx].upper()

    return ''.join(chars_list)


def to_weird_case(string):
    words_list = string.split()

    for idx, word in enumerate(words_list):
        if (idx + 1) // 3 >= 1 and (idx + 1) % 3 == 0:
            words_list[idx] = replace_characters(word)

    return ' '.join(words_list)

original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)

print(to_weird_case(''))