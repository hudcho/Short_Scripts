#Simple script that brute forces an affine cipher shift. This version assumes that the multiplier, A, is known and that ciphertext is also known
#Iterates through 26 shift possibilites for B allowing you to quickly see which shift provides readable english



def decrypt(ciphertext, A, B):
    plaintext = "" 
    for char in ciphertext:
        if char.isalpha():
            x = ord(char.upper()) - ord('A') 
            A_inv = pow(A, -1, 26) 

            ptNum = A_inv * (x - B) % 26
            
            ptChar = chr(ptNum + ord('A'))
            plaintext += ptChar if char.isupper() else ptChar.lower()
        else:
            plaintext += char
    return plaintext

def bruteForceIt (ciphertext, A):
    for B in range(26):
        plaintext = decrypt(ciphertext, A, B)
        print(f"Shift is {B}: {plaintext}")
    
ciphertext = input("Enter ciphertext: ")
multiplier = int(input("Enter multiplier: "))
bruteForceIt(ciphertext, multiplier)

