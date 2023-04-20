import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
# cast the chars to a list
chars = list(chars)
# create a key that we will shuffle
key = chars.copy()

# shuffle the key
random.shuffle(key)

# check available characters
# print(f"chars   : {chars}")
# print(f"key     : {key}")

# ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Original Message    : {plain_text}")
print(f"Encrypted Message   : {cipher_text}")

# DECRYPT
cipher_text = input("Enter a message to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Original Message    : {cipher_text}")
print(f"Encrypted Message   : {plain_text}")