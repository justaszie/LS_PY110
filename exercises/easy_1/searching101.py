""" Problem 
Write a program that solicits six (6) numbers from the user and prints a message that describes whether the sixth number appears among the first five.

PROBLEM
Inputs: number
Outputs: 
Rules:
    - Explicit: 
        - Output message has the following format: 
            {6th number} {is/isn't} in {First 5 numbers separated by a comma}.
    - Implicit:
        - Based on TC, assuming inputs only integer numbers (negative or positive)
        - Assuming user inputs will always be correct type (integer numbers). They won't be validated
        - Numbers can be repeated

EXAMPLES/TEST CASES: N/A 
DATA STRUCTURE: list of 5 numbers, string for the 6th number
ALGORITHM
Create an empty list
Repeat 5 times:
    1. Ask user for a number
    2. Add number to the list 
Ask user for a number6
Check if the number6 is in the list of 5 numbers.
Print the corect output based on whether number6 is in the list or not


"""
def get_prompt(index):
    if index == 6: 
        return "Enter the last number: "
    
    match idx:
        case 1:
            suffix = 'st'
        case 2:
            suffix = 'nd'
        case 3:
            suffix = 'rd'
        case _:
            suffix = 'th'
    return f"Enter the {index}{suffix} number: "


numbers_list = []
for idx in range(1, 6):
    num = input(get_prompt(idx))
    numbers_list.append(num)

number6 = input(get_prompt(6))
list_str = ','.join(numbers_list)

output = f"{number6} is in {list_str}." if number6 in numbers_list else f"{number6} isn't in {list_str}."

print(output)

