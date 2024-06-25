# Chapter 11: Regular expressions
"""
Exercise 2: 
Write a program to look for lines of the form:

New Revision: 39772

Extract the number from each of the lines using a regular expression
and the findall() method. Compute the average of the numbers and
print out the average as an integer.

Enter file:mbox.txt
38549

Enter file:mbox-short.txt
39756
"""
numbers =[]
import re

fname = input('Enter the file name: ')
try: 
    fhand = open(fname)
except: 
    print ('File cannot be opened:', fname)
    exit()

for line in fhand:
    line = line.rstrip()
    x = re.findall('^New Revision: ([0-9]+)', line)
    if len(x) > 0:
        # Convert the found strings to integers and add to the list
        for number in x:
            numbers.append(int(number))

# Define a function to calculate the average
def Average(lst):
    return sum(lst) / len(lst)

if len(numbers) > 0:
    average = Average(numbers)
    print("Average of the list =", int(average))



    

