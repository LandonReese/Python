inputText = ""
N = 0       # number of positions to shift characters in the inputText by. N>=1
D = 0       # direction of shift, D can be either be 1 (right) or -1 (left)

inputText = input("Enter a string: ")
N = input("Enter an integer: ")
Dmy_int2 = input("Enter another integer: ")

# Note that the int() function is used to convert the user input 
# from a string to an integer.
# int(inputText)

for char in inputText:
    print(ord(char))