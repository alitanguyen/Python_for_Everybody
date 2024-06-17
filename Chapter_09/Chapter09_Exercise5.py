# Chapter 9: Dictionaries
"""
Exercise 5: 
This program records the domain name (instead of the address) where
the message was sent from instead of who the mail came from (i.e., the whole email
address). At the end of the program, print out the contents of your dictionary.

python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

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
        domain = word.split("@",2)[1]   # Split email at the "@" character. Use [1] to accesses the second element of the list
        if domain not in counts:
            counts[domain] = 1
        else:
            counts[domain] += 1
print(counts)

