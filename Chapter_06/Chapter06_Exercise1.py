#Chapter 6: Strings
"""
Exercise 1: Write a while loop that starts at the last character in the string and
works its way backwards to the ﬁrst character in the string, printing each letter on
a separate line, except backwards.

"""
fruit = 'orange'
index = 0
while index < len(fruit):
    letter = fruit[(-index - 1)]
    print(letter)
    index = index + 1





                     
    



