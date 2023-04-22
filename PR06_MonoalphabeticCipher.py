# Alphabet mapping example of a Monoalphabetic Cipher
# plaintext to ciphertext
#   # every letter is mapped 1 to 1
#   plain   = ABCDEFGHIJKLMNOPQRSTUVWXYZ
#   cipher  = ZEBRASCDFGHIJKLMNOPQTUVWXY
#   in this case its: A=Z B=E and so on..
#   example:
#   plain   = THIS IS SUPER SECRET
#   cipher  = QDFP FP PTMAO PABOAQ

import string

plaintext = "the quick brown fox jumps over the lazy dog"
key = "zebraistpdcfghjklmnoquvwxy"
# the key should not have repeated letter,
# then fill it up with the rest of the unused letters of the alphabet
cipher = ""


for i in plaintext:
    # ord = is a function that returns the numerical equivalent
    #       of the letter in the ascii table : a = 97 ... z = 122
    #print(ord(i) - ord('a'))
    # we want to start our index at 0 not 97 so we minus ord('a')
    # to the value of the indexed character
    #NOTE : there is a -65 value that will appear.. that was the
    #Space that have a ascii value of 32: 32-97 = -65

    # so to skip that iteration of spaces and any special character
    # we enclose it to an if statement to check if the character is a letter(lower case)
    if i in string.ascii_lowercase:
        index = ord(i) - ord('a')
        #print(ord(i) - ord('a'))

        # now that we get the index of the character,
        # we will convert the equivalent value of it on the key
        # then add it to our cipher
        cipher = cipher + key[index]
    else:
        # just append the character if it is not a letter
        cipher = cipher + i

print("plaintext    : "+plaintext)
print("cpihertext   : "+cipher)
