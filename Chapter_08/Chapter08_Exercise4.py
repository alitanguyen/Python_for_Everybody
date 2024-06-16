# Chapter 8: Lists
"""
Exercise 4: 
Shakespeare used over 20,000 words in his works. But how would you determine that? 
How would you produce the list of all the words that Shakespeare used?
Would you download all his work, read it and track all unique words by hand?
Let’s use Python to achieve that instead. List all unique words, sorted in alphabet-
ical order, that are stored in a ﬁle romeo.txt containing a subset of Shakespeare’s work.

To get started, download a copy of the ﬁle www.py4e.com/code3/romeo.txt. 
Create a list of unique words, which will contain the ﬁnal result. Write a program to
open the ﬁle romeo.txt and read it line by line. 

For each line, split the line into a list of words using the split function. 
For each word, check to see if the word is already in the list of unique words. 
If the word is not in the list of unique words, add it to the list. 
When the program completes, sort and print the list of unique words in alphabetical order.

Enter file: romeo.txt
['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
'and', 'breaks', 'east', 'envious', 'fair', 'grief',
'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
'sun', 'the', 'through', 'what', 'window',
'with', 'yonder']
"""

new_list = []

fhand = open('romeo.txt')
for word in fhand: 
    result = word.split()
    for unique_word in result: 
        if unique_word not in new_list: 
                new_list.append(unique_word)
                
new_list.sort()
print(new_list)



        
            


    
    






