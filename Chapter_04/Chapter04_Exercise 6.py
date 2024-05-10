# Chapter 4: Functions
"""
Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and
create a function called computepay which takes two parameters (hours and rate).

Enter Hours: 45
Enter Rate: 10
Pay: 475.0
"""

def computePay(hours, rate):
    if hours > 40:
        overtime_hours = hours - 40
        regular_pay = 40 * rate
        overtime_pay = overtime_hours * (1.5 * rate)
        total_pay = regular_pay + overtime_pay
    else:
        total_pay = hours * rate
    
    return total_pay  

hours_input = float(input("Enter Hours: ")) 
rate_input = float(input("Enter Rate: "))   

pay = computePay(hours_input, rate_input) # Call the computePay function 

print("Pay:", pay )


