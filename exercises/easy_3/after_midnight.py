"""
PROBLEM
- Inputs: integer - number of minutes 
- Outputs: string - time of day
- Explicit Rules:
    - Input time of day = number of minutes before / after mindnight. 
        - If >0 => time is after midningt. 
        - If <= 0 => time is before midnight. 
    - Output string format is in 24h format (hh:mm)
    - Input can be any integer: negative, 0 or positive 
    - We do not care about standard time, daylight savings or other time rules 
    - We can't use datetime module 
- Implicit Rules:
    - If input equals 0, the output is midnight (00:00)
    - In case of value > 1440 (full day): We will use (value % 1440)
    - In case of value < -1440: We will use -(-value % 1440)
- Questions
    - Time is greater than total minutes in a day or less than -total minutes in a day. 
    I.e. > 1440 or < 1440. - ANSWERED IN TEST CASES 

value = 3000. We will use 120. So time is 02:00
value = -4231. We wll use -1351. So time is 1440-1351 = 89 = 01:29

EXAMPLES
print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True

DATA STRUCTURES
- Integers
- Strings

ALGORITHM
1. Normalize the time to account for multiple days.
    A. If the time is >= 1440, we will use time % 1440
    B. If the time is <= -1440, we will use time % -1440
2. We calculate the time of day in the format of minutes past midnight. 
    - If the input time >= 0:
        time of day in minutes = 0 + input time 
    - Else:
        time of day in minutes = 1440 - input time
3. Convert the time of day in minutes to hours and minutes
    - hours = time of day in minutes / 60 (integer part)
    - minutes = time of day in minutes remainder op 60 
4. Convert the time of day in hours and minutes to string. Use the format "{hh}:{mm}"

If we add time to 1440 as starting point.
    - 1440 + 35 = 
    - 1440 + -5 = 

IMPLEM
- divmod

"""


def pad_zero(quantity):
    if quantity < 10:
        return '0' + str(quantity)
    else:
        return str(quantity)

def time_of_day(minutes_diff):
    if minutes_diff >= 1440:
        minutes_diff %= 1440
    elif minutes_diff <= -1440:
        minutes_diff %= -1440

    tod_minutes = 0 + minutes_diff if minutes_diff >= 0 else 1440 - abs(minutes_diff)

    hours, minutes = divmod(tod_minutes, 60)
    return f"{pad_zero(hours)}:{pad_zero(minutes)}"


print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True


"""
FURTHER EXPLORATION - we can use datetime this time. 
Approach: 
1. High level algo steps 
2. Find the best methods to achieve the steps 

"""