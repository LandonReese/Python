# #Write Function 1 power(a,b,p) that returns a^b mod p using Python’s 
# pow function. Handle special case if b == 1 
# def power(a, b, p): 
#     <Enter your code here> 
def power(a, b, p):
    if (b == 1):
        return a;
    else:
        return pow(a,b,p)
 

# #Write Function 2 that generates and returns a public key using P,G, 
# and a privateKey chosen by the sender 
# def dh_generatePublicKey(P,G,privateKey): 
#     <Enter your code here>  
def dh_generatePublicKey(P, G, privateKey):
    return pow(G, privateKey, P)
    #Your code for this function (copy from your lab5 submission)
    
# #Write Function 3 that generates and returns a private key using the 
# publicKey, privateKey and P chosen by the sender 
# def dh_generateSecretKey(publicKey, privateKey, P): 
#     <Enter your code here>
def dh_generateSecretKey(publicKey, privateKey, P):
    return pow(publicKey, privateKey, P)
    
# Main Function
def main(): 
    P = 0; 
    G = 0; 
    x = 0; #x is Alice's public key
    a = x; 
    y = 0; #y is Bob's public key
    b = 0; 
    ka = 0; #ka is Alice's secret key
    kb = 0; #ka is Bob's secret key
   
    # Both the users will be agreed upon the public keys G and P   
    P = 23; # A prime number P is taken  
    print("The value of P:", P);   
   
    G = 9; # A primitive root for P, G is taken  
    print("The value of G:", G);   
   
    # Alice will choose the private key a   
    a = 4; # a is the chosen private key   
    print("The private key a for Alice:", a);  
    # Enter code here which calls the appropriate function from above 
    # to generate public key for Alice 
    x = dh_generatePublicKey(P, G, a)
       
    # Bob will choose the private key b  
    b = 3; # b is the chosen private key  
    print("The private key b for Bob:", b);  
    # Enter code here which calls the appropriate function from above 
    # to generate public key for Bob> 
    y = dh_generatePublicKey(P, G, b)
  
    # Generating the secret key after the exchange of keys  
    # Enter code here which calls the appropriate function from above 
    # to generate secret keys for both Alice and Bob. Test that these keys 
    # match
    ka = dh_generateSecretKey(y, a, P)
    kb = dh_generateSecretKey(x, b, P)
    print("Secret key for the Alice is:", ka);  
    print("Secret Key for the Bob is:", kb);  
        
if __name__ == '__main__': 
    main()