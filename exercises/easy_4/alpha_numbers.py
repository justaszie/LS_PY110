"""
PROBLEM
- Input: list of integers between 0 and 19
- Output: same list but with integers sorted based on their english word in an alphabetical order
- Explicit Rules:
    - Integers have an english word associated to them: 0 = zero, 1 = one, etc.
    - The list should be sorted alphabetically based on the word value of an integer
- Implicit Rules
    - sorting is done in ascending order
    - Assumption that empty list will return an empty list
    - Assumption: we don't need to validate that number is >0 and <=19
- Questions:
    - Should the function mutate the input object? 
    - Can the list be empty?

EXAMPLES
print(alphabetic_number_sort(
   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]))
# [8, 18, 11, 15, 5, 4, 14, 9, 19, 1, 7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

print(alphabetic_number_sort(
   [0, 1, 4,]) 
# [4, 1, 0]

DATA STRUCTURES
Lists
Dictionary:
{1: 'one',
2: 'two',
...}

ALGORITHM
1. Sort the input list by using the word values corresponding to each integer of the list. 
2. Return the list 

IMPLEM NOTES.
- A list of word representations maps to the integer value. I.e.

[zero, one]: zero is index 0, one is index 1. 
We can use .index(x) method to find the int value 
or we can use indexing to find the word value words[x]

If we had no sort function we'd have to:
1. Build mapping between integer and word. 
2. Create a list that replaces integer with word value
3. Sort the list manually
4. In the sorted list, Replace the word values back with integer values 
"""

def alphabetic_number_sort(numbers):
    words = [
        'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
        'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',
        'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
        'nineteen'
        ]
    
    numbers.sort(key = lambda x: words[x])

    return numbers


print(alphabetic_number_sort(
   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]))
# [8, 18, 11, 15, 5, 4, 14, 9, 19, 1, 7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

print(alphabetic_number_sort([0, 1, 4,])) 
# [4, 1, 0]
