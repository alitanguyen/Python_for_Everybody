# Chapter 6: Strings
"""
Exercise 5: Slicing strings
Take the following Python code that stores a string:
str = 'X-DSPAM-Confidence: 0.8475'
Use find and string slicing to extract the portion of the string after the colon
character and then use the float function to convert the extracted string into a
ﬂoating point number.
"""
str = 'X-DSPAM-Confidence: 0.8475'
start = str.find(' ')
print(start)

end = str.find('5')
print(end)

extraced_string = str[start+1:end+1]
floating_point_number = float(extraced_string)

print(floating_point_number)








                     
    



