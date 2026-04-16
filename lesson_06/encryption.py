import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
print(chars)

chars = list(chars)
key = chars.copy()

random.shuffle(key)
print(f"chars: {chars}")
print(f"key: {key}")


#Encryption
original_message = input("Enter a message to encrypt: ")
encrypted_message = ""

for letter in original_message:
    index = chars.index(letter)
    encrypted_message += key[index]

print(f"original message: {original_message}")
print(f"encrypted message: {encrypted_message}")


#Decrypt
encrypted_input = input("Enter a message to decrypt: ")
decrypted_message = ""

for letter in encrypted_input:
    index = key.index(letter)
    decrypted_message += chars[index]

print(f"encrypted message: {encrypted_input}")
print(f"decrypted message: {decrypted_message}")