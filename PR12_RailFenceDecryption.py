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
#key = 3
ciphertext = input("Enter ciphertext: ")
#ciphertext = "WECRLTEERDSOEEFEAOCAIVDEN"
plaintext = ""

length = len(ciphertext)
plaintext = "." * length

cycle = key * 2 - 2
units = length // cycle     # the // integer division or floor division that returns the whole number quotient after dividing

rail_lengths = [0] * key

# top rail length
rail_lengths[0] = units
# intermediate rail length
for i in range(1, key - 1):
    rail_lengths[i] = 2 * units
# bottom rail length
rail_lengths[key-1] = units

for i in range(length % cycle):
    if i < key:
        rail_lengths[i] += 1
    else:
        rail_lengths[cycle-i] += 1

print(rail_lengths)

print(plaintext)
# replace the characters in the top rail fence
index = 0
rail_offset = 0
for c in ciphertext[:rail_lengths[0]]:
    plaintext = plaintext[:index] + c + plaintext[index+1:]
    index += cycle

rail_offset += rail_lengths[0]
print(plaintext)

# replace characters in the intermediate rails
for row in range(1, key -1):
    left_index = row
    right_index = cycle - row
    left_char = True
    for c in ciphertext[rail_offset:rail_offset+rail_lengths[row]]:
        if left_char:
            plaintext= plaintext[:left_index] + c + plaintext[left_index+1:]
            left_index += cycle
            left_char = not left_char
        else:
            plaintext = plaintext[:right_index] + c + plaintext[right_index + 1:]
            right_index += cycle
            left_char = not left_char
    rail_offset += rail_lengths[row]
    print(plaintext)

# replace characters int the bottom rail fence
index = key - 1
for c in ciphertext[rail_offset:]:
    plaintext = plaintext[:index] + c + plaintext[index + 1:]
    index += cycle

print(plaintext)