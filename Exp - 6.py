def mod_inverse(a, mod=26):
    a %= mod
    for x in range(1, mod):
        if (a * x) % mod == 1:
            return x
    return -1


def decrypt_char(ch, a, b):
    if not ch.isalpha():
        return ch
    ch = ch.upper()
    y = ord(ch) - ord('A')
    a_inv = mod_inverse(a)
    if a_inv == -1:
        return '?'
    p = (a_inv * (y - b + 26)) % 26
    return chr(p + ord('A'))


def solve_key(c1, c2, p1, p2):
    diff_p = (p1 - p2 + 26) % 26
    diff_c = (c1 - c2 + 26) % 26
    inv = mod_inverse(diff_p)
    if inv == -1:
        return None
    a = (diff_c * inv) % 26
    b = (c1 - (a * p1 % 26) + 26) % 26
    return a, b


# ================= MAIN =====================

ciphertext = "BUBUBUBUBUBUBUBUBUBU"
p1, c1 = 4, 1
p2, c2 = 19, 20

result = solve_key(c1, c2, p1, p2)

if result is None:
    print("Unable to find valid 'a'. Decryption not possible.")
else:
    a, b = result
    print(f"Recovered Key: a = {a}, b = {b}")

    plaintext = ''.join(decrypt_char(ch, a, b) for ch in ciphertext)
    print(f"Decrypted Text: {plaintext}")
