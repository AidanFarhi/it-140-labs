"""
Many user-created passwords are simple and easy to guess. 
Write a program that takes a simple password and makes it 
stronger by replacing characters using the key below, 
and by appending "q*s" to the end of the input string.

i becomes !
a becomes @
m becomes M
B becomes 8
o becomes .
Ex: If the input is:

mypassword
the output is:

Myp@ssw.rdq*s
"""

# get original password from standard input
weak_password = input()

# initialize strong password and a dict of replacement characters
strong_password = ''
replacement_characters = {
    'i': '!',
    'a': '@', 
    'm': 'M',
    'B': '8',
    'o': '.'
}

# iterate through weak password and generate strong password
# using replacement characters
for character in weak_password:
    if character in replacement_characters:
        strong_password += replacement_characters[character]
    else:
        strong_password += character
strong_password += 'q*s'

# print strong password to standard output
print(strong_password)
