#Chapter 5: Iteration 
"""
Exercise 1: Write a program which repeatedly reads integers until the user enters “done”. 
Once “done” is entered, print out the total, count, and average of the integers. 
If the user enters anything other than a integers, detect their mistake
using try and except and print an error message and skip to the next integers.

Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Enter a number: 7
Enter a number: done
16 3 5.333333333333333
"""
##########################################################
# Solution 1: 
##########################################################

total = 0 
count = 0  
average = 0 
line = ''
while line != 'done':
        line = input('Enter a number: ') # Ask for input
        try:
            total = total + int(line) # Calculate total amount
            count = count + 1 
            average = total / count 
        except ValueError: 
            if line == 'done':
                break 
            else:
                print('Invalid data')              
print('Total:', total)
print('Count:', count)
print('Average:', average)

##########################################################
# Solution 2: 
##########################################################

total = 0 
count = 0  
average = 0 
line = ''
while line != 'done':
        line = input('Enter a number: ') # Ask for input
        try:
            total = total + int(line) # Calculate total amount
            count = count + 1 
            average = total / count 
        except ValueError: 
            if line != 'done':
                print('Invalid data')              
print('Total:', total)
print('Count:', count)
print('Average:', average)

##########################################################
# Solution 3: 
##########################################################

total = 0
count = 0
average = 0 

while True:
    line = input ('Enter a number: ') # Ask for input
    try:
        if line != "done":
            total = total + int(line)
            count = count + 1
            average = total / count

        else:
            print ("Total: " + str(total))
            print ("Count: " + str(count))
            print ("Average: " + str(average))
            
    except ValueError:
        print('Invalid input')

##########################################################
# Solution 4: 
##########################################################

numbers = []  # Initialize an empty list which is used to store entered numbers
while True:
    try:
        line = input('Enter a number: ') 
        if line == 'done':
            total = sum(numbers)
            count = len(numbers)
            average = total / count 
            print("Total:", total)
            print("Count:", count)
            print("Average:", average)
            break

        number = int(line)
        numbers.append(number) # Store each entered number to the data structure in order to perform necessary calculations
        
    except ValueError:
       print('Invalid input')