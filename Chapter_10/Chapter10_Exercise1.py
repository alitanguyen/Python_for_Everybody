# Chapter 10: Tuples
"""
Exercise 1: 

Revise a previous program as follows: Read and parse the “From”
lines and pull out the addresses from the line. Count the number of messages from
each person using a dictionary.
After all the data has been read, print the person with the most commits by
creating a list of (count, email) tuples from the dictionary. Then sort the list in
reverse order and print out the person who has the most commits.

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195
"""

# Step 1: Count the number of messages from each person using a dictionary
fname = input('Enter a file name: ')
try: 
    fhand = open(fname)
except:  
    print('File cannot be opned:', fname)
    exit()

counts = dict()

for line in fhand: 
    words = line.split() 
    if len(words) == 0: continue        # Skip blank lines
    if words[0] != 'From': continue     # Skip lines that do not start with 'From'
    for word in [words[1]]:       
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

# Step 2: Print the person with the most commits by creating a list of (count, email) tuples from the dictionary
l = list()

for key, value in counts.items():
    l.append((value, key))

l.sort(reverse=True)
max_key, max_value = max(l)

print(max_value, max_key)




