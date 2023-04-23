# sample 1 = WEAREDISCOVEREDFLEEATONCE
# W . . . E . . . C . . . R . . . L . . . T . . . E
# . E . R . D . S . O . E . E . F . E . A . O . C .
# . . A . . . I . . . V . . . D . . . E . . . N . .
# rails = 3 : Cipher = WECRLTEERDSOEEFEAOCAIVDEN
#
# sample 2 = THIS*IS*TOP*SECRET
# T . . . . . . . T . . . . . . . E .
# . H . . . . . * . O . . . . . R . T
# . . I . . . S . . . P . . . C . . .
# . . . S . I . . . . . * . E . . . .
# . . . . * . . . . . . . S . . . . .
# rails =5 : Cipher = TTEH*ORTISPCSI*E*S

key = int(input("Enter key(number of rails): "))
plaintext = input("Enter plaintext: ")
ciphertext = ""

cycle = key * 2 - 2

for row in range(key):
    index = 0

    # first rail
    if row == 0:
        while index < len(plaintext):
            ciphertext += plaintext[index]
            index += cycle

    # last rail
    elif row == key - 1:
        index = row
        while index < len(plaintext):
            ciphertext += plaintext[index]
            index += cycle

    # middle rows
    else:
        # we need two indexes here because the middle rails
        # have 2 different cadence before printing the letter
        # example on rail 2 of sample 2 : THIS*IS*TOP*SECRET
        # . H . . . . . * . O . . . . . R . T
        # there are 2 cadence : 2 and 6
        left_index = row
        right_index = cycle - row
        while left_index < len(plaintext):
            ciphertext += plaintext[left_index]

            if right_index < len(plaintext):
                ciphertext += plaintext[right_index]

            left_index += cycle
            right_index += cycle

# check
print(ciphertext)