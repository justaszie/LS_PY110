"""
PROBLEM
- Input: String representing first name and last name 
- Output: String representing first name and last name in reverse order
- Explicit Rules:
    - Input argument is a string containing first name, a space and last name
    - Output should have the format of "{last name}, {first name}"
- Implicit Rules:
    - Assumption: output case should be the same as input
    - Assumption: input will always contain at least 2 words and a space between
    - Assumption: if the input has more words, only the 2 first words are included in the output.
    - Assumption: the return value is a new string, not the original modified.
- Questions:
    - Case should be respected?
    - Should we validate that input has the right format? 
    - New object

EXAMPLES
print(swap_name('Joe Roberts'))    # "Roberts, Joe"

DATA STRUCTURES
Strings 
Lists

ALGORITHM
1. Split the input string into a list of words using the whitespace as separator
2. Create a new string with the last element of the list, a whitespace and first element of the list
3. Return the new string
"""

# def swap_name(full_name):
#     first_name, last_name = full_name.split()
#     return f"{last_name}, {first_name}"


# print(swap_name('Joe Roberts'))    # "Roberts, Joe"

"""
FURTHER EXPLORATION 
What if the person has one or more middle names? 
Refactor the current solution so that it can accommodate this; 
the middle names should be listed after the first name:

Output format:
"{last name}, {first name} {middle names}"
names_list[-1], names_list[0], names_list[1:len(names_list) - 1]
if names_list longer than 2, append names_list [1:]
[joe, robberts] => robberts. joe, 


1. Get list of words
2. Create a new result list with last element of the original list, followed by the first element of the original list
3. If original list is longer than 2 elements:
    - Append the result list with all the elements until the last element of original list, excluded
4. Create a string from the resulting list of words
5. Return the new string 


"""
def swap_name(full_name):
    names_list = full_name.split()
    result = ', '.join([names_list[-1], names_list[0]])
    if len(names_list) > 2:
        result += ' ' + ' '.join(names_list[1:-1])
    return result


print(swap_name('Karl Oskar Henriksson Ragvals'))    # "Ragvals, Karl Oskar Henriksson"