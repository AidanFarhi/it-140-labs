"""
Write a program that first reads in the name of an input file and then reads the input file
using the file.readlines() method. The input file contains an unsorted list of number of 
seasons followed by the corresponding TV show. Your program should put the contents of the 
input file into a dictionary where the number of seasons are the keys, and a list of TV shows 
are the values (since multiple shows could have the same number of seasons).

Sort the dictionary by key (least to greatest) and output the results to a file named 
output_keys.txt, separating multiple TV shows associated with the same key with a semicolon 
(;). Next, sort the dictionary by values (alphabetical order), and output the results to a 
file named output_titles.txt.

Ex: If the input is:

file1.txt
and the contents of file1.txt are:

20
Gunsmoke
30
The Simpsons
10
Will & Grace
14
Dallas
20
Law & Order
12
Murder, She Wrote
the file output_keys.txt should contain:

10: Will & Grace
12: Murder, She Wrote
14: Dallas
20: Gunsmoke; Law & Order
30: The Simpsons
and the file output_titles.txt should contain:

Dallas
Gunsmoke
Law & Order
Murder, She Wrote
The Simpsons
Will & Grace
"""

# Define constants
OUTPUT_KEYS_FILE_NAME = 'output_keys.txt'
OUTPUT_TITLES_FILE_NAME = 'output_titles.txt'

# Instantiate a dictionary to store seasons and shows
seasons_shows = {}

# Get file name from standard input
input_file_name = input()

# TODO: Write a proper explaination here
with open(input_file_name, 'r') as file:
    lines = [str.strip(l) for l in file.readlines()]
    for i, line in enumerate(lines):
        if i % 2 == 0: # season number
            if seasons_shows.get(int(line), None) is None:
                seasons_shows[int(line)] = []
        else: # show name
            seasons_shows[int(lines[i-1])].append(line)

# Write each key and value in the desired format
with open(OUTPUT_KEYS_FILE_NAME, 'w') as output_keys_file:
    for season, shows in sorted(list(seasons_shows.items()), key=lambda x: x[0]):
        output_keys_file.write(f"{season}: {'; '.join(shows)}\n")
