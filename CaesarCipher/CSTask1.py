def customEncrypt():# => int:
    inputText = ""

inputText = ""
reverseText = ""
encryptedText = ""
N = 0       # number of positions to shift characters in the inputText by. N>=1
D = 0       # direction of shift, D can be either be 1 (right) or -1 (left)

inputText = input("Enter a string: ")
# for char in inputText:
#     if int(char) = 32 or int(char) = 33:

N = int(input("Enter a positive integer: "))
while N <= 0:
    N = int(input("Invalid input. Please enter a positive integer: "))

D = int(input("Enter 1 (Right shift) or -1 (Left shift): "))
while D != 1 and D != -1:
    D = int(input("Invalid input. Enter 1 (Right shift) or -1 (Left shift): "))

# Note that the int() function is used to convert the user input 
# from a string to an integer.
# int(inputText)


# 1. Reverse the input text
reverseText = "".join(reversed(inputText))
print("inputText:     " + inputText)
print("reverseText:   " + reverseText)

# 2. Shift all the ASCII characters in reversed input text by “N” positions.
for char in reverseText:
    x = ord(char)           # x is the ASCII value of our character
    y = N * D               # N * D = Our shift amount in the positive or negative direction
    x += y                  # x is now an incremented ascii value
    #lets say x = 45, shifted left 20. x now is 25
    while x < 34:
        x+=126
    while x > 126:
        x-=126
    # print(x)
    character = chr(x)
    # print(character)
    encryptedText = encryptedText + character

print("encryptedText: " + encryptedText)