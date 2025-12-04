#Caesar Cipher (Shift k)

def caesar_encrypt(text, k):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + k) % 26 + base)
        else:
            result += ch
    return result

text = input("Enter text: ")
shift = int(input("Enter shift (1-25): "))
print("Encrypted:", caesar_encrypt(text, shift))
