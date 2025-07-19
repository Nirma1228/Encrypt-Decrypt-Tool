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
print("🔐 Caesar Cipher Tool 🔐")
choice = input("Do you want to (e)ncrypt or (d)ecrypt? ")
