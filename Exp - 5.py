#Affine Cipher + Validity Check

import math

def affine_encrypt(text, a, b):
    result = ""
    for ch in text.lower():
        if ch.isalpha():
            result += chr((a*(ord(ch)-97)+b)%26 + 97)
        else:
            result += ch
    return result

def valid_a(a):
    return math.gcd(a, 26) == 1

a = int(input("Enter a: "))
b = int(input("Enter b: "))

if not valid_a(a):
    print("Invalid 'a': must be coprime with 26")
else:
    msg = input("Enter plaintext: ")
    print("Cipher:", affine_encrypt(msg, a, b))
