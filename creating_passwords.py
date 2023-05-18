"""
(1) Prompt the user to enter two words and a number, storing each into separate variables. Then, output those three values on a single line separated by a space. (Submit for 1 point)

Ex: If the input is:

yellow
Daisy
6
the output after the prompts is:

You entered: yellow Daisy 6
Note: User input is not part of the program output.


(2) Output two passwords using a combination of the user input. Format the passwords as shown below. (Submit for 2 points, so 3 points total).

Ex: If the input is:

yellow
Daisy
6
the output after the prompts is:

You entered: yellow Daisy 6

First password: yellow_Daisy
Second password: 6yellow6

(3) Output the length of each password (the number of characters in the strings). (Submit for 2 points, so 5 points total).

Ex: If the input is:

yellow
Daisy
6
the output after the prompts is:

You entered: yellow Daisy 6

First password: yellow_Daisy
Second password: 6yellow6

Number of characters in yellow_Daisy: 12
Number of characters in 6yellow6: 8
"""

# Get word1, word2, and integer from input
word1 = input('Enter first word:\n')
word2 = input('Enter second word:\n')
integer = input('Enter an integer:\n')

# Generate password options
first_password = f'{word1}_{word2}'
second_password = f'{integer}{word1}{integer}'

# Print output
print(f'You entered:', ' '.join([word1, word2, integer]))
print()
print(f'First password: {first_password}')
print(f'Second password: {second_password}')
print()
print(f'Number of characters in {first_password}: {len(first_password)}')
print(f'Number of characters in {second_password}: {len(second_password)}')
