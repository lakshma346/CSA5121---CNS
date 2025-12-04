#Polyalphabetic (Vigenère Cipher)

def vigenere_encrypt(text, key):
    result = ""
    key_idx = 0
    for ch in text:
        if ch.isalpha():
            shift = ord(key[key_idx % len(key)].lower()) - ord('a')
            base = ord('a')
            result += chr((ord(ch.lower()) - base + shift) % 26 + base)
            key_idx += 1
        else:
            result += ch
    return result

plain = input("Enter plaintext: ")
key = input("Enter key: ")
print("Ciphertext:", vigenere_encrypt(plain, key))
