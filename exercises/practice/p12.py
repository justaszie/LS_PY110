"""
PROBLEM
- Input: string
- Output: True / False if the string is pangram or not
- Rules:
    - Pangram: sentences that contain every letter of the alphabet at least once
    - Matching letters is case-insensitive
- Questions
    -


ALGORITHM
Create a list of alphabet letters.
    - Iterate over code point values starting from (a) to (z) and append each letter to list
As we go through string, "tick-off" the letters.
    - If the letter is in the list of alphabet letters, remove it from the list
    (case insensitive matching)
At the end if any alphabet letters remain, it's not panagram


"""
def get_alphabet():
    start = ord('a')
    end = ord('z')
    # return [ chr(x) for x in range(start, end + 1) ]
    return [ x for x in range(start, end + 1) ]

def is_pangram(sentece):
    alphabet = get_alphabet()
    for char in sentece:
        if ord(char.lower()) in alphabet:
            alphabet.remove(ord(char.lower()))
        # if char.lower() in alphabet:
        #     alphabet.remove(char.lower())

    return not alphabet

print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
print(is_pangram(my_str) == True)

