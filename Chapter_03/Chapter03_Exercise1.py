# Chapter 3: Conditional execution
"""
Exercise 1: Rewrite your pay computation to give the employee 1.5 times the
hourly rate for hours worked above 40 hours.

Enter Hours: 45
Enter Rate: 10
Pay: 475.0
"""

hour = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))
if hour < 40: 
    print("Pay:", hour * rate)
else:
    print("Pay:", (40 * rate) + (hour - 40) * rate * 1.5)


