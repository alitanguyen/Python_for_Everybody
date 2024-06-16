# Chapter 9: Dictionaries
"""
Exercise 1: Download a copy of the ﬁle
www.py4e.com/code3/words.txt
Write a program that reads the words in words.txt and stores them as keys in
a dictionary. It doesn’t matter what the values are. Then you can use the in
operator as a fast way to check whether a string is in the dictionary.

"""
fhand = open('words.txt')
dictionary_words = dict()               # Create a new dictionary

for line in fhand:                      # Loop through each line in the file
    words = line.split()                # Break each line into a list of words 
    for word in words:
        dictionary_words[word] = True   # Add each word to the dictionary (using the word as the key, with a value of True)

# Check whether a string is in the dictionary. 
# For example, check whether 'Writing' is in the dictionary. 
if 'Writing' in dictionary_words:
    print('True')
else:
    print('False')

# For example, check whether 'Python' is in the dictionary. 
if 'writing' in dictionary_words:
    print('True')
else:
    print('False')


