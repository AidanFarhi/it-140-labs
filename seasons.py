"""
Write a program that takes a date as input and outputs the date's season. 
The input is a string to represent the month and an int to represent the day.

Ex: If the input is:

April
11
the output is:

Spring
In addition, check if the string and int are valid (an actual month and day).

Ex: If the input is:

Blue
65
the output is:

Invalid 

The dates for each season are:
Spring: March 20 - June 20
Summer: June 21 - September 21
Autumn: September 22 - December 20
Winter: December 21 - March 19
"""

from calendar import monthrange
from datetime import date

# Get month and day from standard input
input_month = input()
input_day = int(input())

# Create a dictionary to use as a lookup for month numbers and month name ranges
months = {
    'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 
    'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12
}

# Use conditional logic to determine the season
current_year = date.today().year
season = None
if input_day < 1:
    season = 'Invalid'
elif input_month in months and monthrange(current_year, months[input_month])[1] < input_day:
    season = 'Invalid'
elif input_month in list(months.keys())[:3]:
    season = 'Spring' if input_month == 'March' and input_day >= 20 else 'Winter'
elif input_month in list(months.keys())[3:6]:
    season = 'Summer' if input_month == 'June' and input_day >= 21 else 'Spring'
elif input_month in list(months.keys())[6:9]:
    season = 'Autumn' if input_month == 'September' and input_day >= 22 else 'Summer'
elif input_month in list(months.keys())[9:]:
    season = 'Winter' if input_month == 'December' and input_day >= 21 else 'Autumn'
else:
    season = 'Invalid'

# Print output
print(season)
