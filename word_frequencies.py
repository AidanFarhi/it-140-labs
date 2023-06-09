"""
Write a program that reads a list of words. Then, the program outputs those words and their frequencies.

Ex: If the input is:

hey hi Mark hi mark
the output is:

hey 1
hi 2
Mark 1
hi 2
mark 1
"""

# Get words from standard input
words = input().split()

# Create a dictionary of word frequencies
frequencies = {}
for word in words:
    frequencies[word] = frequencies.get(word, 0) + 1

# Print result to standard output
for word in words:
    print(word, frequencies[word])
