# Chapter 9: Dictionaries
"""
Exercise 2: Write a program that categorizes each mail message by which day of
the week the commit was done. To do this look for lines that start with “From”,
then look for the third word and keep a running count of each of the days of the
week. At the end of the program print out the contents of your dictionary (order
does not matter).
Sample Line:

From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

Sample Execution:

python dow.py
Enter a file name: mbox-short.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}
"""
######################################################
# SOLUTION 1
######################################################

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
    for word in words[2].split():       # Split the string to words using whitespace characters (including tabs and newlines) as delimiters
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print(counts)

######################################################
# SOLUTION 2
######################################################

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
    for word in [words[2]]:             
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print(counts)



