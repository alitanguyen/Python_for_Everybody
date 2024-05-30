# Chapter 7: Files
"""
Exercise 2: Write a program to prompt for a ﬁle name, and then read through the ﬁle and look for lines of the form:

X-DSPAM-Confidence: 0.8475

When you encounter a line that starts with “X-DSPAM-Conﬁdence:” pull apart the line to extract the ﬂoating-point number on the line. 
Count these lines and then compute the total of the spam conﬁdence values from these lines. 
When you reach the end of the ﬁle, print out the average spam conﬁdence.

Enter the file name: mbox.txt
Average spam confidence: 0.894128046745

Enter the file name: mbox-short.txt
Average spam confidence: 0.750718518519

Test your ﬁle on the mbox.txt and mbox-short.txt ﬁles.
"""

input = input('Enter a file name: ')
total = 0 
count = 0 
average = 0 
if input == 'mbox.txt':
        fhand = open('C:/Users/9360/Desktop/Python/mbox.txt')
        for line in fhand:
            if line.find('X-DSPAM-Confidence:') == -1: continue
            index = line.find(' ') # Find the first empty space in the line
            extract_Number = line[index:] # Use string slicing to extract the ﬂoating-point number on the line
            total = total + float(extract_Number) 
            count = count + 1
            average = total / count 
        print('Average spam confidence:', average)
    
elif input == 'mbox-short.txt':
    fhand = open('C:/Users/9360/Desktop/Python/mbox-short.txt')
    for line in fhand:
            if line.find('X-DSPAM-Confidence:') == -1: continue
            index = line.find(' ') # Find the first empty space in the line
            extract_Number = line[index:] # Use string slicing to extract the ﬂoating-point number on the line
            total = total + float(extract_Number) 
            count = count + 1
            average = total / count 
    print('Average spam confidence:', average)
