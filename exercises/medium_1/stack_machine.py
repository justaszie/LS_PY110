"""
PROBLEM 
- Input: a program string
- Output: actions taken depending on program instructions
- Explicit Rules:
    - All input strings are valid programs 
    * stack = list that gets elements appended and popped (remove last added) LIFO 
    * register = currently stored value (short term memory)
    * operation that takes 2 values:
        1. takes 1st value from stack (pops last added) 
        2. uses register value as the 2nd value
        3. replaces the current register value with the operation result 
    * 1 value ops: 
        - POP (removes from stack and puts in register)
        - PRINT (print reg value)
        - n place integer n to reg
        - PUSH: appends reg value to stack (leaves reg value)
    * 2 value ops:
        - ADD
        - SUB (register - stack)
        - MULT
        - DIV (reg / stack) - integer only 
        - REMAINDER (reg / stack) - int remainder only
        - 
    - Stack value and register value are initialized to [] and 0 
- Implicit:
    - Stack and register are initialized for each program. There is no carryover values between separate programs. 
    - Instructions in the program string are separated by spaces 

EXAMPLES
Provided


DATA STRUCTURES
- String as a progrma
- List of strings for separate instructions 
- Some strings converted to integers to be used as values
- list to represent stack
- integer to represent register value 

ALGORITHM 
1. Set stack value to empty list
2. Set register value to 0
3. Split the program string into a list of instructions
4. Iterate over each instruction string. For each value, take action depending on its format:
    A. If the string contains just digits:
        - convert the string to integer value
        - place the integer value in the register
    B. If the string is 'PUSH':
        - append the current register value to the stack 
    C. If the string is 'POP':
        - remove the last element of the stack and assign it to the register variable
    D. If the string is 'PRINT':
        - display the current register value 
    E. If the string is 'ADD': 
        - Remove the last stack value and assign it to a temp variable
        - Set register value to {current register value + last stack value}
    F. If the string is 'SUB': 
        - Remove the last stack value and assign it to a temp variable
        - Set register value to {current register value - last stack value}
    G. If the string is 'MULT': 
        - Remove the last stack value and assign it to a temp variable
        - Set register value to {current register value * last stack value}
    H. If the string is 'DIV': 
        - Remove the last stack value and assign it to a temp variable
        - Set register value to the integer part of the {current register value / last stack value} operation
    I. If the string is 'REMAINDER': 
        - Remove the last stack value and assign it to a temp variable
        - Set register value to the integer remainder part of the {current register value MOD last stack value} operation


IMPLEM NOTES
- potentially use match case 
"""

def minilang(program):
    print('STARTING THE PROGRAM')
    stack = []
    register = 0

    instructions = program.split()

    for instruction in instructions:
        if instruction.isdigit() or instruction.startswith('-'):
            register = int(instruction)
        elif instruction == 'PUSH':
            stack.append(register)
        elif instruction == 'PRINT':
            print(register)
        elif instruction == 'POP':
            register = stack.pop()
        else:
            last_stack_element = stack.pop()
            match instruction:
                case 'ADD':
                    register += last_stack_element
                case 'SUB':
                    register -= last_stack_element
                case 'MULT':
                    register *= last_stack_element
                case 'DIV':
                    register //= last_stack_element
                case 'REMAINDER':
                    register %= last_stack_element
    print('COMPLETED THE PROGRAM')

# minilang('PRINT')
# # 0

# minilang('5 PUSH 3 MULT PRINT')
# # 15

# minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# # 5
# # 3
# # 8

# minilang('5 PUSH POP PRINT')
# # 5

# minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# # 5
# # 10
# # 4
# # 7

# minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# # 6

# minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# 12

minilang('-3 PUSH 5 SUB PRINT')
# 8

# minilang('6 PUSH')
# (nothing is printed)