def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char
    return result

def decrypt(cipher_text, shift):
    return encrypt(cipher_text, -shift)

# Command-line interface
print(" Caesar Cipher Tool ")
choice = input("Do you want to (e)ncrypt or (d)ecrypt? ")

if choice.lower() == 'e':
    plain_text = input("Enter the text to encrypt: ")
    shift_value = int(input("Enter the shift value (number): "))
    encrypted = encrypt(plain_text, shift_value)
    print(f"🔒 Encrypted Text: {encrypted}")
