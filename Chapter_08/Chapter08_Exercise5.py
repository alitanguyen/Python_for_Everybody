# Chapter 8: Lists
"""
Exercise 5: 
Imagine you wrote a minimalist email app, that lists the email
of the senders in the user’s Inbox and counts the number of emails.
Write a program to read through the mail box data and when you ﬁnd line that
starts with “From”, you will split the line into words using the split function. We
are interested in who sent the message, which is the second word on the From line.

From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

You will parse the From line and print out the second word for each From line,
then you will also count the number of From (not From:) lines and print out a
count at the end. This is a good sample output with a few lines removed:

python fromcount.py
Enter a file name: mbox-short.txt
stephen.marquard@uct.ac.za
louis@media.berkeley.edu
zqian@umich.edu

[...some output removed...]

ray@media.berkeley.edu
cwen@iupui.edu
cwen@iupui.edu
cwen@iupui.edu
There were 27 lines in the file with From as the first word
"""
fname = input('Enter a file name: ')
fhand = open('mbox-short.txt') 
count = 0

for line in fhand: 
    words = line.split()
    if len(words) == 0: continue # Skip to the next line if there is a line without any words
    if words[0] != 'From': continue # Skip to the next line if there is a line which does not have 'From' as its first word
    list = words[1]
    count = count + 1
    print(list)

print('There were', count, 'lines in the file with From as the first word')
    



        
            


    
    






