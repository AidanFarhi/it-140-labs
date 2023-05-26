"""
Given a line of text as input, output the number of characters excluding spaces, 
periods, or commas.

Ex: If the input is:

Listen, Mr. Jones, calm down.
the output is:

21
Note: Account for all characters that aren't spaces, periods, 
or commas (Ex: "r", "2", "!").
"""
import re

# substitute unwanted characters from text recieved from standard
# input and print the length to standard output.
print(len(re.sub(r'[ ,.]', '', input())))
