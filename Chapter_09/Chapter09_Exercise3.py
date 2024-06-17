# Chapter 9: Dictionaries
"""
Exercise 3:
Write a program to read through a mail log, build a histogram using
a dictionary to count how many messages have come from each email address, and
print the dictionary.

Enter file name: mbox-short.txt
{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
'ray@media.berkeley.edu': 1}

"""
fname = input('Enter a file name: ')
try: 
    fhand = open(fname)
except: 
    print('File cannot be opned:', fname)
    exit()

counts = dict()

for line in fhand: 
    words = line.split() 
    if len(words) == 0: continue        # Skip to the next line if there is a blank line
    if words[0] != 'From': continue     # Skip to the next line if there is a line which does not have 'From' as its first word
    for word in [words[1]]:       
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print(counts)
