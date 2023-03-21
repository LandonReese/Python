#Jupyter Notebook 1
def testCustomEncrypt():
    invalid = True  #initializing as True
    inputText = input("Enter a username: ")
    while invalid:
        invalid = False #not invalid, until proven invalid
        for char in inputText:
            if ord(char) == 32 or ord(char) == 33:
                print("Please enter a username without ' ' or '!': ")
                invalid = True
    print(inputText)
    print()
    
testCustomEncrypt()