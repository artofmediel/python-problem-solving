# in vigenere cipher, you don't have a mapping(letter to letter equivalent),
# just a scret phrase
import string

plaintext = "the quick brown fox jupms over the lazy dog"
key= "lemon"
cipher = ""

index = 0

for i in plaintext:
    if i in string.ascii_lowercase:
        offset = ord(key[index]) - ord('a')
        # check
        #print(offset)
        # we need modulo sign to wrap around the length of the alphabet
        encrypted_cipher = chr(((ord(i) - ord('a') + offset) % 26) + ord('a'))
        cipher = cipher + encrypted_cipher

        index = (index + 1) % len(key)
    else:
        cipher = cipher + i

print("plaintext :" + plaintext)
print("cipher    :" + cipher)

# DECRYPTION
print("--------------------------------")
decrypted_text = ""

decryption_index = 0

decryption_key = input("Enter decryption key :")

for i in cipher:
    if i in string.ascii_lowercase:
        offset = ord(decryption_key[decryption_index]) - ord('a')
        # POSITIVE OFFSET
        positive_offset = 26 - offset
        decrypted_i = chr((ord(i) - ord('a') - offset) % 26 + ord('a'))

        #-------------------
        # NEGATIVE OFFSET
        #negative_offset= ord(i) - ord('a') - offset
        #if negative_offset <0:
        #    negative_offset = negative_offset + 26
        #decrypted_i = chr(negative_offset + ord('a'))

        decrypted_text = decrypted_text + decrypted_i
        # we need modulo sign to wrap around the length of the key
        decryption_index = (decryption_index + 1) % len(decryption_key)

    else:
        decrypted_text = decrypted_text + i

print("cipher    :" + cipher)
print("decrypted :" + decrypted_text)