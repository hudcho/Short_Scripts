"""
Program: AffineCipherBruteForce.py
Author: Hudson Cho
Date: 09.01.25
Description: Simple script to brute force an affine cipher when the multiplier
             (alpha) is known

Usage: Enter ciphertext and multiplier (alpha), look in output for readable english text
Requirements: Python 3.8+ (for modular inverse with pow)
"""

def decrypt(ciphertext, A, B):
    """ 
        Decrypts ciphertext A using the affine decrytpion formula

        Finds modular inverse of A using pow(A, -1, 26), although the extended euclidean algorithm would also work here
        Applies this to formula A_inv * (x - B) % 26 = plaintext

        Args:
            ciphertext: encoded ciphertext
            A: multiplier alpha that was used in the affine encryption alg to encrypt ciphertext
            B: Shift value B that was used in affine encryption alg to encrypt ciphertext
        Returns:
            plaintext: decryped plaintext
    """
    plaintext = "" 
    for char in ciphertext:
        if char.isalpha():
            x = ord(char.upper()) - ord('A') 
            A_inv = pow(A, -1, 26) #Value erorr thrown if there exists a gcd(A,26) != 1

            ptNum = A_inv * (x - B) % 26
            
            ptChar = chr(ptNum + ord('A'))
            plaintext += ptChar if char.isupper() else ptChar.lower()
        else:
            plaintext += char
    return plaintext

def bruteForceIt (ciphertext, A):
    """
        Calls upon decrypt 26 times to try every shift value that B can take on (0-25)

        Args:
            ciphertext: encrpyted ciphertext
            A: Known multiplier (alpha) that was used in the encryption process
    """
    for B in range(26):
        plaintext = decrypt(ciphertext, A, B)
        print(f"Shift is {B}: {plaintext}")
    
ciphertext = input("Enter ciphertext: ")
multiplier = int(input("Enter multiplier: "))
bruteForceIt(ciphertext, multiplier)
