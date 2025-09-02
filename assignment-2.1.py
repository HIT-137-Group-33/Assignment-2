import string

# Helper function to shift a character
def shift_char(c, shift, forward=True):
    if c.islower():
        alphabet = string.ascii_lowercase
    elif c.isupper():
        alphabet = string.ascii_uppercase
    else:
        return c  # leave unchanged
    
    idx = alphabet.index(c)
    if forward:
        new_idx = (idx + shift) % 26
    else:
        new_idx = (idx - shift) % 26
    return alphabet[new_idx]


# Encryption function
def encrypt_file(shift1, shift2):
    with open("raw_text.txt", "r", encoding="utf-8") as f:
        raw_text = f.read()
    
    encrypted_text = ""
    for c in raw_text:
        if c.islower():
            if c <= 'm':  # first half
                encrypted_text += shift_char(c, shift1 * shift2, forward=True)
            else:  # second half
                encrypted_text += shift_char(c, shift1 + shift2, forward=False)
        elif c.isupper():
            if c <= 'M':  # first half
                encrypted_text += shift_char(c, shift1, forward=False)
            else:  # second half
                encrypted_text += shift_char(c, shift2 ** 2, forward=True)
        else:
            encrypted_text += c  # leave unchanged
    
    with open("encrypted_text.txt", "w", encoding="utf-8") as f:
        f.write(encrypted_text)


# Decryption function
def decrypt_file(shift1, shift2):
    with open("encrypted_text.txt", "r", encoding="utf-8") as f:
        encrypted_text = f.read()
    
    decrypted_text = ""
    for c in encrypted_text:
        if c.islower():
            if c <= 'm':  # originally shifted forward
                decrypted_text += shift_char(c, shift1 * shift2, forward=False)
            else:  # originally shifted backward
                decrypted_text += shift_char(c, shift1 + shift2, forward=True)
        elif c.isupper():
            if c <= 'M':  # originally shifted backward
                decrypted_text += shift_char(c, shift1, forward=True)
            else:  # originally shifted forward
                decrypted_text += shift_char(c, shift2 ** 2, forward=False)
        else:
            decrypted_text += c  # unchanged
    
    with open("decrypted_text.txt", "w", encoding="utf-8") as f:
        f.write(decrypted_text)


# Verification function
def verify():
    with open("raw_text.txt", "r", encoding="utf-8") as f1, \
         open("decrypted_text.txt", "r", encoding="utf-8") as f2:
        raw_text = f1.read()
        decrypted_text = f2.read()
    
    if raw_text == decrypted_text:
        print("✅ Decryption successful: Original and decrypted texts match.")
    else:
        print("❌ Decryption failed: Files do not match.")


# Main program
def main():
    shift1 = int(input("Enter shift1 value: "))
    shift2 = int(input("Enter shift2 value: "))
    
    encrypt_file(shift1, shift2)
    print("Encryption complete. Encrypted text saved to 'encrypted_text.txt'.")
    
    decrypt_file(shift1, shift2)
    print("Decryption complete. Decrypted text saved to 'decrypted_text.txt'.")
    
    verify()


if __name__ == "__main__":
    main()
