"""
PROBLEM
- Inputs: float number representing angle (between 0 and 360)
- Outputs: string representing the angle in degrees, minutes and seconds

- Explicit Rules:
    - Input value can't be negative
    - Output should include symbols for different units:
        - ° for degrees
        - ' for minutes
        - " for seconds
    - 1 degree = 60 minutes
    - 1 minute = 60 seconds
    - Symbol code for DEGREE: DEGREE = "\u00B0" 

- Implicit Rules:
    - Convert partial degrees to minutes and seconds. E.g. 0.73 deg = 43.8min = 43 min + 0.8 * 60(48) seconds. 
    - Unless they have a specific value, the minutes and seconds have '00' value by default
    - Single - digit minute and seconds values are represent with leading 0 - e.g. '05' minutes
    - Single - digit degree values are represented with a single value (e.g. '0' degrees)
    - escape sequences may be necessary as output string will contain both single abd double quotes

- Questions:
    - Assumption: Single - digit degree values are represented with a single value (e.g. '5' degrees)
    - Assumption: Number will always be between 0 and 360 inclusive. no input validation is needed


EXAMPLES
30 => "30°00'00\""
76.73 => "76°43'48\""
93.034773 => "93°02'05\""
0 => "0°00'00\""
5 => "5°00'00\""


DATA STRUCTURES:
- Floats for input and interim calculations for degrees, minutes and seconds
- Strings for output 

ALGORITHM:
1. Convert the value to integer (keeping only the int part) and assign it to degree value
2. Get the decimal part of the input value (input value - integer part)
3. If the decimal part == 0:
    - construct a result string with the degree value, appropriate symbols and 00 for both minutes and seconds
    - return the result string
3. get minutes value from the decimal part 
    - decimal part of input * 3600 // 60
4. get seconds value from the decimal part 
    - decimal part of input * 3600 % 60 
5. convert minutes value to string representation
    - If the value < 10, add leading 0 character to string
6. convert seconds value to string representation
    - If the value < 10, add leading 0 character to string
7. construct result string wit the string values for degree, minute, second string representations and appropriate symbols
8. return result string. 




IMPLEMENTATION
- Pay attention to any float imprecision. This test case may cause issues: print(dms(93.034773) == "93°02'05\"") 
- Use a constant for DEGREE symbol.
    DEGREE = "\u00B0" 

""" 

"""
FURTHER EXPLORATION 
refactor it so that it works with any positive or negative number

print(dms(-1))   # 359°00'00"
print(dms(400))  # 40°00'00"
print(dms(-40))  # 320°00'00"
print(dms(-420)) # 300°00'00"

- Input: any positive or negative float number 
- Output: Same as normal solution 
- Explicit rules:
    - Input can be less than 0 or greater than 360
- Implicit Rules:
    - When input value is greater than 360, we should use the degree value of (input - 360)
    - TBD - when value is less than 0

- Questions: 
    - How do we calculate the degrees for negative values (a) greater than -360, (b) less than -360 

EXAMPLES





"""

def dms(degree_float):
    degree_int = int(degree_float)
    decimal = degree_float - degree_int
    
    minutes = int(decimal * 3600 // 60)
    seconds = int(decimal * 3600 % 60)

    degrees_str = f"{degree_int}{DEGREE}"
    
    minutes_str = f"{minutes}'"
    if minutes < 10:
        minutes_str = '0' + minutes_str
    
    seconds_str = f"{seconds}\""
    if seconds < 10:
        seconds_str = '0' + seconds_str
    
    return f"{degrees_str}{minutes_str}{seconds_str}"

def dms_fe(degree_float):
    normalized_degree = degree_float % 360 

    return dms(normalized_degree)

    # decimal = degree_float - degree_int

    # if decimal == 0:
    #     return f"{degree_int}{DEGREE}00'00\""
    
    # minutes = int(decimal * 3600 // 60)
    # seconds = int(decimal * 3600 % 60)

    # degrees_str = f"{degree_int}{DEGREE}"
    
    # minutes_str = f"{minutes}'"
    # if minutes < 10:
    #     minutes_str = '0' + minutes_str
    
    # seconds_str = f"{seconds}\""
    # if seconds < 10:
    #     seconds_str = '0' + seconds_str
    # # print(f"{degrees_str}{minutes_str}{seconds_str}")
    # return f"{degrees_str}{minutes_str}{seconds_str}"

DEGREE = "\u00B0"

# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")
print(dms(-420))

print(dms_fe(-1))   # 359°00'00"
print(dms_fe(400))  # 40°00'00"
print(dms_fe(-40))  # 320°00'00"
print(dms_fe(-420)) # 300°00'00"
print(dms_fe(-40.52)) # 300°00'00"


