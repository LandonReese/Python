#Jupyter Notebook 1
def testCustomEncrypt():
    userId = ""
    encryptId = ""
    userPassword = ""
    encryptPassword = ""
    invalid = True  #initializing as True
    userId = input("Enter a username: ")
    while invalid:
        invalid = False #not invalid, until proven invalid
        for char in userId:
            if ord(char) == 32 or ord(char) == 33:
                print("Please enter a username without a ' ' or an '!': ")
                invalid = True
    
    userPassword = input("Enter a password: ")
    # Unblock this code if the password is not allowed to have a ' ' or an '!'
    # while invalid:
    #     invalid = False #not invalid, until proven invalid
    #     for char in userPassword:
    #         if ord(char) == 32 or ord(char) == 33:
    #             print("Please enter a password without a ' ' or an '!': ")
    #             invalid = True
    
    N = int(input("Enter a positive integer for a shift amount: "))
    while N <= 0:
        N = int(input("Invalid input. Please enter a positive integer: "))

    D = int(input("Enter 1 (Right shift) or -1 (Left shift): "))
    while D != 1 and D != -1:
        D = int(input("Invalid input. Enter 1 (Right shift) or -1 (Left shift): "))
        
    encryptId = "".join(reversed(userId))
    encryptPassword = "".join(reversed(userPassword))
    
    y = N * D # y = The amount and direction to shift
    eString = "" #temp variable
    for char in encryptId:
        x = ord(char)           # x is the ASCII value of our character
        x += y                  # x is now an incremented ascii value
        
        while x < 34:
            x+=126
        while x > 126:
            x-=126
        
        character = chr(x)
        eString = eString + character
    encryptId = eString
    
    eString = "" #re-initialize temp prior to use
    for char in encryptPassword:
        x = ord(char)           # x is the ASCII value of our character
        x += y                  # x is now an incremented ascii value
        
        while x < 34:
            x+=126
        while x > 126:
            x-=126
        
        character = chr(x)
        eString = eString + character
    encryptPassword = eString
    
    print("userId:          " + userId)
    print("reversedId:      " + userPassword)
    print("encryptedId:     " + encryptId)
    print("encryptPassword: " + encryptPassword)
    
testCustomEncrypt()