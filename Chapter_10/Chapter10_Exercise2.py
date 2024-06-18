# Chapter 10: Tuples
"""
Exercise 2: 

This program counts the distribution of the hour of the day for each
of the messages. You can pull the hour from the “From” line by ﬁnding the time
string and then splitting that string into parts using the colon character. Once
you have accumulated the counts for each hour, print out the counts, one per line,
sorted by hour as shown below.

python timeofday.py
Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
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
    if len(words) == 0: continue        # Skip blank lines
    if words[0] != 'From': continue     # Skip lines that do not start with 'From'
    for word in [words[5]]: 
        hour = word.split(":")[0]       # Split the time at the ":" character. Use [0] to accesses the first element of the string
        if hour not in counts:
            counts[hour] = 1
        else:
            counts[hour] += 1

l = list()
for key, value in counts.items():
    l.append((key, value))

l.sort()

for key, value in l:
    print(key, value)
    



