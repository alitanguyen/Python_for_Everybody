# Chapter 3: Conditional execution
"""
Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the
program. The following shows two executions of the program:

Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input

Enter Hours: forty
Error, please enter numeric input
"""

try: 
    hour = input('Enter Hours: ')   
    hour = float(hour) 

    rate = input('Enter Rate: ')
    rate = float(rate)

    print("Pay:", hour * rate)
    
except: 
    print('Error, please enter numeric input')



