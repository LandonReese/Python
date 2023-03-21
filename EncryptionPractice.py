# Landon Reese Notes from Lab Handout
#
# This function first takes the input from the user and then evaluates the expression, which
# means Python automatically identifies whether user entered a string or a number or list. If
# the input provided is not correct then either syntax error or exception is raised by python.
def input():
    num = input ("Enter number :")
    print(num)
    name1 = input("Enter name : ")
    print(name1)

# Python ord() function takes string argument of a single Unicode character and return its
# integer Unicode code point value.
def ord():
    x = ord('A')
    print(x)
    print(ord('ć'))
    print(ord('ç'))
    print(ord('$'))
    
#Python chr() function takes integer argument and return the string representing a character
# at that code point.
def chr():
    y = chr(65)
    print(y)
    print(chr(123))
    print(chr(36))
