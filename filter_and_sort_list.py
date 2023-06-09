"""
Write a program that gets a list of integers from input, 
and outputs non-negative integers in ascending order (lowest to highest).

Ex: If the input is:

10 -7 4 39 -6 12 2
the output is:

2 4 10 12 39 
For coding simplicity, follow every output value by a space. Do not end with newline.
"""

# Get numbers from standard input
numbers = [int(n) for n in input().split()]

# Filter out non-negative numbers and sort
result = sorted(list(filter(lambda x: x >= 0, numbers)))

# Print result to standard output
for n in result:
    print(n, end=' ')