import sys
import numpy as np

def cipher_decryption(cipher, key):  
    encryp_text = cipher 
    finalDeletion = False
    
    # Handle condition if the message length is odd.
    if len(cipher) % 2 == 1:
        # print("odd, appending X")
        encryp_text += "X"
        finalDeletion = True
    # #<Enter code here>
    #
    # Convert msg to matrices
    k = 0   # k is the iterator through our letters
    cols = int(len(encryp_text)/2)
    # print(cols)
    msgMatrix = np.zeros((2, cols), dtype=int)
    for i in range(2):
        for j in range(cols):
            msgMatrix[i, j] = ord(encryp_text[k])
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
    # <Enter code here>
    #
    # finding multiplicative inverse
    encryp_text = ""
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
        encryp_text += chr(text)
        text = (((msgMatrix[0][n] * key2d[1][0]) + (msgMatrix[1][n] * key2d[1][1])) % 26) + 65
        encryp_text += chr(text)
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
    # #<Enter code here>
    #
    # multiplying multiplicative inverse with adjugate matrix
    
    #<Enter code here>
    #
    # Calculate modulo
    
    #<Enter code here>
    #
    # Convert cipher to plaintext
    
    # #<Enter code here>
    
    print("Decrypted text: {}".format(decryp_text))
    
    # Example:
    # plaintext = "Secret Message"
    # plaintext = plaintext.upper().replace(" ","")
    # key = "hill"
    # key = key.upper().replace(" ","")
    # ciphertext = cipher_encryption(plaintext, key)
    # cipher_decryption(ciphertext, key)