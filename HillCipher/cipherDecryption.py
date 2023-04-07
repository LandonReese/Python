import sys
import numpy as np

def cipher_decryption(cipher, key):  
    decryp_text = cipher 
    finalDeletion = False
    
    # Handle condition if the message length is odd.
    if len(cipher) % 2 == 1:
        # print("odd, appending X")
        decryp_text += "X"
        finalDeletion = True
    # #<Enter code here>
    #
    # Convert msg to matrices
    k = 0   # k is the iterator through our letters
    cols = int(len(decryp_text)/2)
    # print(cols)
    msgMatrix = np.zeros((2, cols), dtype=int)
    for i in range(2):
        for j in range(cols):
            msgMatrix[i, j] = ord(decryp_text[k])
            k += 1
    # <Enter code here>
    #
    # Convert key to 2x2
    k = 0
    key2d = np.zeros((2, 2), dtype=int)
    for i in range(2):
        for j in range(2):
            key2d[i, j] = ord(key[k])
            k += 1
    # #<Enter code here>
    #
    # Decrement values by 65, 'A", so modulus math works
    for i in range(2):
        for j in range(2):
            key2d[i, j] -= 65
            msgMatrix[i, j] -= 65
                    
    # finding determinant
    # key2d = [[A, B],
    #          [C, D]]
    # A * D - B * C
    d = (key2d[0][0] * key2d[1][1]) - (key2d[1][0] * key2d[0][1])
    d = d % 26
    if d == 0:
        print("Determinant is zero, there is no inverse")
        
    # Calculate the determinant inverse
    dinv = -99
    for i in range(26):
        if(d * i) % 26 == 1:
            dinv = i
            print("dinv:", dinv)
    if(dinv == -99):
        print("Not found")
        return "No inverse for the determinant"
            
    
    # <Enter code here>
    #
    # finding multiplicative inverse
    decryp_text = ""
    # ranges: msgMatrix[0,1][0,1,2,3,4,5,6, etc]
    #         key2d[0,1][0,1]
    # i in range cols is 0-6...etc in msgMatrix range
    # Total range = r[0-1][0-n]
    # r[0,0] r[1,0]
    # r[0,1] r[1,1]
    # r[0,2] r[1,2]
    # r[0,n] r[1,n]
    for n in range(cols):
        text = (((msgMatrix[0][n] * key2d[0][0]) + (msgMatrix[1][n] * key2d[0][1])) % 26) + 65
        decryp_text += chr(text)
        text = (((msgMatrix[0][n] * key2d[1][0]) + (msgMatrix[1][n] * key2d[1][1])) % 26) + 65
        decryp_text += chr(text)
    #<Enter code here>
    #
    # find transpose
    transposedMatrix = np.transpose(key2d)
    # find minor
    minorMatrix = np.zeros((2, 2), dtype=int)
    minorMatrix[0][0] = key2d[1][1]
    minorMatrix[0][1] = key2d[0][1]
    minorMatrix[1][0] = key2d[1][0]
    minorMatrix[1][1] = key2d[0][0]
    # <Enter code here>
    #
    # #changing signs
    minorMatrix[0][1] *= -1
    minorMatrix[0][1] *= -1
    minorMatrix[0][1] = minorMatrix[0][1] % 26
    minorMatrix[1][0] = minorMatrix[1][0] % 26
    print("key2d")
    print(key2d)
    print("minorMatrix")
    print(minorMatrix)
    # #<Enter code here>
    
    # multiplying multiplicative inverse with adjugate matrix
    inverseMatrix = (dinv * transposedMatrix) % 26
    print(inverseMatrix)
    #<Enter code here>
    #
    # Calculate modulo
    
    #<Enter code here>
    #
    # Convert cipher to plaintext
    
    # #<Enter code here>
    decryp_text = ""
    for n in range(cols):
        text = (((msgMatrix[0][n] * inverseMatrix[0][0]) + (msgMatrix[1][n] * inverseMatrix[0][1])) % 26) + 65
        decryp_text += chr(text)
        text = (((msgMatrix[0][n] * inverseMatrix[1][0]) + (msgMatrix[1][n] * inverseMatrix[1][1])) % 26) + 65
        decryp_text += chr(text)
    # <Enter code here>
    
    # If message length was odd, reduce length by 1
    if(finalDeletion):
        # print(decryp_text)
        decryp_text = decryp_text[:-1]
        
    print("Decrypted text: {}".format(decryp_text))
    
    # Example:
    # plaintext = "Secret Message"
    # plaintext = plaintext.upper().replace(" ","")
    # key = "hill"
    # key = key.upper().replace(" ","")
    # ciphertext = cipher_encryption(plaintext, key)
    # cipher_decryption(ciphertext, key)
key = "hill"
ciphertext = "CIQIPMCFLGWTV"
print("Starting")
cipher_decryption(ciphertext, key)