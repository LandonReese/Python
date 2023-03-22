def customEncrypt(text, numN, numD):
    reverseText = ""
    encryptedText = ""
    N = 0       # number of positions to shift characters in the inputText by. N>=1
    D = 0       # direction of shift, D can be either be 1 (right) or -1 (left)

    # 1. Reverse the input text
    reverseText = "".join(reversed(text))

    # 2. Shift all the ASCII characters in reversed input text by “N” positions.
    for char in text:
        x = ord(char)           # x is the ASCII value of our character
        y = numN * numD               # N * D = Our shift amount in the positive or negative direction
        x += y                  # x is now an incremented ascii value
        #lets say x = 45, shifted left 20. x now is 25
        while x < 34:
            x+=126
        while x > 126:
            x-=126
        
        character = chr(x)
        encryptedText = encryptedText + character
        print("Text:    " + text)
        print("Encrypt: " + encryptedText)
    return encryptedText