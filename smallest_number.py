"""
Write a program whose inputs are three integers, and whose output is the smallest of the three values.

Ex: If the input is:

7
15
3

the output is:

3
"""

# Get integers from standard input
x = int(input())
y = int(input())
z = int(input())

# Figure out which one is the smallest
smallest = min(x, y, z)

# Print output
print(smallest)
