"""
Write a program whose input is a string which contains a character and a phrase, and whose output indicates the number of times the character appears in the phrase.

Ex: If the input is:

n Monday
the output is:

1
Ex: If the input is:

z Today is Monday
the output is:

0
Ex: If the input is:

n It's a sunny day
the output is:

2
Case matters.

Ex: If the input is:

n Nobody
the output is:

0
n is different than N.
"""

# Get input and split
char_and_phrase = input().split(' ')

# Extract character and phrase from split input
char = char_and_phrase[0]
phrase = ''.join(char_and_phrase[1:])

# Print output
print(phrase.count(char))
