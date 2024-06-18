# Chapter 10: Tuples
"""
Exercise 3: 

Write a program that reads a ﬁle and prints the letters in decreasing order of frequency.

Your program should convert all the input to lower case and only count the letters
a-z. Your program should not count spaces, digits, punctuation, or anything other
than the letters a-z. 

Find text samples from several diﬀerent languages and see how letter frequency varies between languages. 

Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.
"""
import string

fname = input('Enter a file name: ')
try: 
    fhand = open(fname)
except:  
    print('File cannot be opned:', fname)
    exit()

counts = dict()

# Create a translation table that remove both punctuation and digits
translation_table = str.maketrans('', '', string.punctuation + string.digits)
        
# Process each line in the file
for line in fhand:
    line = line.translate(translation_table)  # Remove all punctuations and digits
    line = line.lower()
    words = line.split()
    for word in words:
        for character in word: 
            if character not in counts: 
                counts[character] = 1
            else: 
                counts[character] += 1

l = list()
for key, value in counts.items():
    l.append((value, key))

l.sort(reverse=True)

for key, value in l:
    print(value, key)

