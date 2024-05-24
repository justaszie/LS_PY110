"""
PROBLEM
- Inputs: a list of elements 
- Outputs: print out the elements and their number of occurance
- Explicit Rules:
    - Counting occurences should be case-sensitive. E.g. "suv" and "SUV" are different words.
    - The counts should be printed out by the function
- Implicit Rules:
    - Print out format : 
    "
    car => 4
    truck => 3
    SUV => 1
    motorcycle => 2
    " 
    - Assumption: elements can only be strings
    - Assumption: if input list is empty, we will print out "List is empty"
    - Assumption: the function has no return value
    - Assumption: empty strings and strings that are only spaces will not be counted 
- Questions:
    - Elements will be only strings?
    - Empty list 
    - Return value ? 
    - Empty strings? 
    - Strings that are only spaces. 

EXAMPLES
# 1) 
vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)

# Output
# our output sequence may appear in a different sequence
# car => 4
# truck => 3
# SUV => 1
# motorcycle => 2

# 2) 
vehicles = []

count_occurrences(vehicles)

# Output
# Empty List


DATA STRUCTURES
    - Input list 
    - Dictionary of counts

ALGORITHM
- High Level 
1. Count the occurences of each word
2. Print out the occurences

- Detailed
1. Create an empty dictionary "counts"
2. Loop through the input list. For each string
    A. If the string is empty:
        - move to next string 
    B. Else:
        i. If the string is present in the counts dictionary:
            - Increment the count of its occurences
        ii. Else:
            - Add the string to the dictionary with count value 1
3. Loop through the values in the dictionary. For each string and count value pair:
    A. Print a line with the following format "{string} => {count}"


IMPLEM NOTES
- dict.setdefault or get() with 0 default 
    
"""
def count_occurrences(strings):
    counts = {}

    if len(strings) == 0:
        print("Empty List")

    for string in strings:
        if string and not string.isspace():
            counts[string] = counts.get(string, 0) + 1

    for string, count in counts.items():
        print(f"{string} => {count}")

# 1) 
vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)

# Output
# our output sequence may appear in a different sequence
# car => 4
# truck => 3
# SUV => 1
# motorcycle => 2

# 2) 
vehicles = []

count_occurrences(vehicles)

# Output
# Empty List

# 3) 
vehicles = ['suv', 'SUV', 'plane', '\t  ', '  ', '', 'truck', '', 'SUV']

count_occurrences(vehicles)

# Output
# suv => 1
# SUV => 2
# plane => 1
# truck =>1


