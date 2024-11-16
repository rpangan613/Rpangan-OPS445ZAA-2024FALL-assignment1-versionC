#!/usr/bin/env python3

'''
OPS445 Assignment 1
Program: assignment1.py 
The python code in this file is original work written by
"Roniel Pangan". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.

Author: Roniel G. Pangan
Semester: Fall Semester 2024
Description: OPS445 - Assignment 1
'''

import sys

def day_of_week(date: str) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    day, month, year = (int(x) for x in date.split('/'))
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + day) % 7
    return days[num]

def leap_year(year: int) -> bool:
    """Return true if the year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def mon_max(month: int, year: int) -> int:
    """Returns the maximum day for a given month. Includes leap year check."""
    if month == 2:
        return 29 if leap_year(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def after(date: str) -> str: 
    '''
    after() -> date for next day in DD/MM/YYYY string format

    Return the date for the next day of the given date in DD/MM/YYYY format.
    This function has been tested to work for year after 1582
    '''
    day, mon, year = (int(x) for x in date.split('/'))
    day += 1  # next day

    lyear = year % 4
    if lyear == 0:
        leap_flag = True
    else:
        leap_flag = False  # this is not a leap year

    lyear = year % 100
    if lyear == 0:
        leap_flag = False  # this is not a leap year

    lyear = year % 400
    if lyear == 0:
        leap_flag = True  # this is a leap year
    
    mon_dict= {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
           7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if mon == 2 and leap_flag:
        mon_max = 29
    else:
        mon_max = mon_dict[mon]
    
    if day > mon_max:
        mon += 1
        if mon > 12:
            year += 1
            mon = 1
        day = 1  # if tmp_day > this month's max, reset to 1 
    return f"{day:02}/{mon:02}/{year}"

def before(date: str) -> str:
    "Returns previous day's date as DD/MM/YYYY"
    day, month, year = (int(x) for x in date.split('/'))
    day -= 1  # go to previous day

    if day == 0:  # need to go back to the last day of the previous month
        month -= 1
        if month == 0:  # wrap around to December of the previous year
            month = 12
            year -= 1
        day = mon_max(month, year)  # get last day of previous month

    return f"{day:02}/{month:02}/{year}"

def usage():
    "Print a usage message to the user"
    print("Usage: " + str(sys.argv[0]) + " DD/MM/YYYY NN")
    sys.exit()

def valid_date(date: str) -> bool:
    """Check validity of date."""
    try:
        day, month, year = (int(x) for x in date.split('/'))
        print(f"Validating date: {day}/{month}/{year}")  # Debug statement

        # Check valid ranges for month
        if month < 1 or month > 12:
            return False

        # Check if the day is within the valid range for the month
        max_day = mon_max(month, year)
        print(f"Max days in month: {max_day}")  # Debug statement
        return day > 0 and day <= max_day
    except ValueError:
        return False

def day_iter(start_date: str, num: int) -> str:
    "iterates from start date by num to return end date in DD/MM/YYYY"
    current_date = start_date
    for _ in range(abs(num)):
        current_date = after(current_date) if num > 0 else before(current_date)
    return current_date

if __name__ == "__main__":
    # Check length of arguments
    if len(sys.argv) != 3:
        usage()

    start_date = sys.argv[1]
    try:
        num_days = int(sys.argv[2])
    except ValueError:
        usage()  # If it can't be converted to an int, show usage

    # Check first arg is a valid date
    if not valid_date(start_date):
        usage()

    # Call day_iter function to get end date
    end_date = day_iter(start_date, num_days)
    
    # Print the result
    print(f'The end date is {day_of_week(end_date)}, {end_date}.')
    # Now we know num_days is a valid integer
    # Call day_iter function to get end date
    end_date = day_iter(start_date, num_days)
    
    # Print the result
    print(f'The end date is {day_of_week(end_date)}, {end_date}.')
