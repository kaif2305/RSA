import random
 
#Tests to see if a number is prime.   
def prime(num):
    for i in range(2,num//2):
        if num%i==0:
            return False
    return True

'''
Euclid's algorithm for determining the greatest common divisor
Use iteration to make it faster for larger integers
'''
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
#Euclid's extended algorithm for finding the multiplicative inverse of two numbers
def mod_inverse(e,phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi//e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return (d + phi)
        
#Generate Co-Prime    
def co_prime():
    list = []
    for i in list_n:
        if gcd(i,n)==1:
            list.append(i)
    return list   

# Generating Public and Private Key
def generate_KeyPair(p,q):
    if (prime(p) and prime(q))==False:
        raise ValueError("_______The Input No's are not Prime________")
    
    e= 13 # Choose an integer e such that e and phi(n) are coprime  
    d = mod_inverse(e, phi) # Use Extended Euclid's Algorithm to generate the private ke
    
    return (e,d)
    
def encrypt(msg_plaintext,public):
    key = public
    # Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [pow(ord(char), key, n) for char in msg_plaintext]
    # Return the array of bytes
    return cipher

    
def decrypt(msg_ciphertext,private):
    # Unpack the key into its components
    key = private
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    aux = [str(pow(char, key, n)) for char in msg_ciphertext]
    # Return the array of bytes as a string
    plain = [chr(int(char2)) for char2 in aux]
    return ''.join(plain)
        

print("Enter 2 Prime NO's")
p=int(input())
q=int(input())

n = p*q
phi = (p-1)*(q-1)

list_n = []
for i in range(2,phi):
    list_n.append(i)

print("Generating public/private keypair...")
public, private = generate_KeyPair(p,q) 
print("Public Key: (",public,",",n,")")
print("Private Key:(",private,",",n,")")
message = input(" - Enter a message to encrypt with your public key: ")
name = []
for i in range(0,len(message),3):
    x = message[i:i+2]
    name.append(x)
 
char = ''
for i in name:
    x = (int(i)+64)%65
    char+= chr(x)
    
print("The Alphabetic referance of the message",char)
encrypted_msg = encrypt(char, public)
print("\n________ENCRYPT________")
print(" - Your encrypted message is: ", ''.join(map(lambda x: str(x), encrypted_msg)))

while(1):
    choice = int(input("\n 1.Decryption \n 2.Exit \n Enter your choice : "))
    if choice ==1:
        print("\n________DECRYPT________")
        encyt = int(input(" - Enter The encrypted message :  "))
        d = int(input("Enter Private Keys : . . .\nd = "))
        n = int(input("n = "))
        print("(",d,",",n,")")
        print(" - Decrypting message with private key ", private, " . . .")
        print(" - Your message is: ", decrypt(encrypted_msg,private))
        print("\n=================END==================")
        break
    else:
        print("\n=================END==================")
        break
