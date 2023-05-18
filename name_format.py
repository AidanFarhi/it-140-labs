"""
Many documents use a specific format for a person's name. Write a program that reads a person's name in the following format:

firstName middleName lastName (in one line)

and outputs the person's name in the following format:

lastName, firstInitial.middleInitial.

Ex: If the input is:

Pat Silly Doe
the output is:

Doe, P.S.
If the input has the following format:

firstName lastName (in one line)

the output is:

lastName, firstInitial.

Ex: If the input is:

Julia Clark
the output is:

Clark, J.
"""

# Get full name from input
full_name = input()

# Split full name
split_name = full_name.split(' ')

# Extract last name and initials
last_name = split_name[-1]
initials = ''.join([f'{x[0]}.' for x in split_name[:-1]])

# Print result
print(f'{last_name}, {initials}')
