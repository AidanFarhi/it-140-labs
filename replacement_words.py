"""
Write a program that replaces words in a sentence. 
The input begins with word replacement pairs (original and replacement). 
The next line of input is the sentence where any word on the original list is replaced.

Ex: If the input is:

automobile car   manufacturer maker   children kids
The automobile manufacturer recommends car seats for children if the automobile doesn't already have one.
the output is:

The car maker recommends car seats for kids if the car doesn't already have one. 
You can assume the original words are unique.
"""

#  Get words, replacements, and sentence from standard input
words_and_replacements = input().split('   ')
sentence = input().split()

# Create a dictionary of words and replacements
replacement_lookup = {}
for word_replacement in words_and_replacements:
    word, replacement = word_replacement.split()
    replacement_lookup[word] = replacement

# Replace words in sentence
for i, word in enumerate(sentence):
    if word in replacement_lookup:
        sentence[i] = replacement_lookup[word]

# Print result to standard output
print(' '.join(sentence))
