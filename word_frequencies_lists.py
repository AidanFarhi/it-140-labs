"""
Write a program that first reads in the name of an input file and then reads the file using the 
csv.reader() method. The file contains a list of words separated by commas. 
Your program should output the words and their frequencies 
(the number of times each word appears in the file) without any duplicates.

Ex: If the input is:

input1.csv
and the contents of input1.csv are:

hello,cat,man,hey,dog,boy,Hello,man,cat,woman,dog,Cat,hey,boy
the output is:

hello 1
cat 2
man 2
hey 2
dog 2
boy 2
Hello 1
woman 1
Cat 1
"""

import csv

# Instantiate a word frequencies dictionary
word_freqs = {}

# Get the name of the file from standard input
file_name = input()

# Open csv file using context manager i.e with open(...) as ...
with open(file_name) as csv_file:
    # Instantiate a csv reader
    csv_reader = csv.reader(csv_file)
    # Read rows
    for row in csv_reader:
        # Process each row
        for word in row:
            word_freqs[word] = word_freqs.get(word, 0) + 1

# Print word counts
for word, count in word_freqs.items():
    print(word, count)

