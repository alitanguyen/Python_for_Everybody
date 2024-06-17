# Chapter 9: Dictionaries
"""
Exercise 4: 
Add code to the above program to ﬁgure out who has the most messages in the ﬁle. 
After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop 
(see Chapter 5: Maximum and minimum loops) to ﬁnd who has the most messages and print how many messages the person has.

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195

"""
##############################################
# SOLUTION 1
##############################################
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

max_key = max(counts, key=counts.get)   # Tell the max function to use the values of the counts dictionary to determine which key is the maximum
print(max_key, counts.get(max_key))         

##############################################
# SOLUTION 2
##############################################
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

def max(counts):
    largest_key = None
    largest_value = None
# Loop through dictionary items:
    for key, value in counts.items():   # .items() helps access both the keys and values at the same time to find the key associated with the largest value.
        if largest_value is None or value > largest_value:
            largest_value = value 
            largest_key = key
    return largest_key, largest_value 

max_key, max_value = max(counts)
print (max_key, max_value)