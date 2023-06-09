"""
Statistics are often calculated with varying amounts of input data. 
Write a program that takes any number of integers as input, and outputs the average and max.

Ex: If the input is:

15 20 0 5
the output is:

10 20
"""

# Get numbers from standard input
numbers = [int(n) for n in input().split()]

# Calculate the average of all numbers in the list and the maximum number
average = int(sum(numbers) / len(numbers))
maximum = max(numbers)

# Print result to standard output
print(average, maximum)
