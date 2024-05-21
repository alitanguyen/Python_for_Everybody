#Chapter 5: Iteration 
"""
Exercise 2: Write a program which repeatedly reads integers until the user enters “done”. 
And at the end prints out both the maximum and minimum of the numbers instead
of the average.

If the user enters anything other than a integers, detect their mistake
using try and except and print an error message and skip to the next integers.

"""
##########################################################
# Solution 1: 
##########################################################

total = 0 
count = 0  
min = None
max = None 
line = ''
while line != 'done':
        line = input('Enter a number: ') # Ask for input
        try:
            total = total + int(line) # Calculate total amount
            count = count + 1 
            if min is None or int(line) < int(min):  
                min = line
            if max is None or int(line) > int(max):
                max = line

        except ValueError: 
            if line == 'done':
                break 
            else:
                print('Invalid data')    

print('Total:', total)
print('Count:', count)
print('Minimum:', min)
print('Maximum:', max)

##########################################################
# Solution 2: 
##########################################################

numbers = [] # Initialize an empty list which is used to store entered numbers
while True:
    try:
        line = input('Enter a number: ')
        if line == 'done':
            total = sum(numbers)
            count = len(numbers)
            max = max(numbers)
            min = min(numbers)
            print("Total:", total)
            print("Count:", count)
            print("Maximum:", max)
            print("Minimum:", min)
            break

        number = int(line)
        numbers.append(number) # Store each entered number to the data structure in order to perform necessary calculation
    except:
       print('Invalid input')

##########################################################
# MISTAKE I HAVE MADE 
##########################################################

total = 0 
count = 0  
min = None
line = ''
while line != 'done':
    line = input('Enter a number: ') # Ask for input
    try:
        total = total + int(line) # Calculate total amount
        count = count + 1 
        if min is None or line < min: # WRONG 
            min = line

    except ValueError: 
        if line == 'done':
            break 
        else:
            print('Invalid data') 

print('Total:', total)
print('Count:', count)
print('Minimum:', min)

#Mistake: Compare 2 strings which is wrong. Example: '10' < '3' is True 
#How to fix: Compare integers only  


                     
    



