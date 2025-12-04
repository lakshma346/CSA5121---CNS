#Monoalphabetic Substitution Cipher

import string

# Generate substitution key
def generate_key():
    plain = list(string.ascii_lowercase)
    cipher = plain[:] 
    cipher.reverse()   # simple substitution mapping a->z, b->y etc
    return dict(zip(plain, cipher))

# Encrypt
def mono_encrypt(text, key):
    result = ""
    for ch in text.lower():
        if ch in key:
            result += key[ch]
        else:
            result += ch
    return result

# Decrypt
def mono_decrypt(text, key):
    reverse = {v: k for k, v in key.items()}
    result = ""
    for ch in text.lower():
        if ch in reverse:
            result += reverse[ch]
        else:
            result += ch
    return result

# --- MAIN ---
key = generate_key()
msg = input("Enter message: ")

cipher = mono_encrypt(msg, key)
plain = mono_decrypt(cipher, key)

print("Cipher Text:", cipher)
print("Decrypted Text:", plain)
