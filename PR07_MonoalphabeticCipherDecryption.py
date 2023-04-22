import string

key = "zebraistpdcfghjklmnoquvwxy"
cipher = "ota lqpbc emjvh ijw dqgkn juam ota fzyx rjs"
plaintext = ""

# iterate through the cipher
for i in cipher:
    # check if the character on index is a letter :
    # if not then just append on the plaintext
    if i in string.ascii_lowercase:
        # use the character's index and store it to a variable to check
        index = key.find(i)
        # check
        # print(index)
        # now, we add ord('a') to the index on the chr function,
        # because 'a' on ascii starts at 97, not 0
        # chr() gets an ascii index then returns the letter equivalent
        # append its value to the plaintext
        plaintext += chr(index + ord('a'))
    else:
        plaintext = plaintext + i

# display result
print("cipher: " + cipher)
print("plaintext: " + plaintext)
