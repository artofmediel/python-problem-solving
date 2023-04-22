import string

# enclose the cipher in a function
def key_matrix_generation(key):
    letters_lc = string.ascii_lowercase.replace('j', '.')

    key_matrix = ['' for i in range(5)]

    index = 0
    PF_row_index = 0

    for i in key:
        if i in letters_lc:
            key_matrix[index] += i
            # we need to remove duplicate letters
            letters_lc = letters_lc.replace(i, '.')
            # check the progression
            #print(letters_lc)

            # iterate through the rows of the playfair matrix
            PF_row_index +=1
            # increment index :
            # if row index is on the 5th column, reset index
            if PF_row_index > 4:
                index += 1
                PF_row_index = 0

    # add the remaining letters from the letters_lc to the key matrix
    for i in letters_lc:
        # do not include the characters replaced by '.'
        if i != '.':
            key_matrix[index] += i

            PF_row_index += 1
            if PF_row_index > 4:
                index += 1
                PF_row_index = 0

    # return the key_matrix value
    return key_matrix

# check
key_matrix = key_matrix_generation('playfair example')
print(key_matrix)

# -----------------------------------------------------

plaintext = "hidethegoldinthetreestump"
plaintextpairs = []
ciphertextpairs = []

# RULES:
# Apply Rule 1. If both letters are the same (or only 1 letter
# is left), Add an 'X' after the first letter

i=0
while i < len(plaintext):
    a = plaintext[i]
    b = ''
    if(i + 1) == len(plaintext):
        b = 'x'
    else:
        b = plaintext[i+1]

    if a != b:
        plaintextpairs.append(a+b)
        i += 2
    else:
        plaintextpairs.append(a+'x')
        i += 1

print(plaintextpairs)



for pair in plaintextpairs:
    applied_rule = False
    # Apply Rule 2. If the letters appear on the same row of your
    # table, replace them with the letters to their immediate right
    # respectively
    for row in key_matrix:
        if pair[0] in row and pair[1] in row:
            firstpair = row.find(pair[0])
            secondpair = row.find(pair[1])

            ciphertextpair = row[(firstpair + 1)%5] + row[(secondpair + 1)%5]
            ciphertextpairs.append(ciphertextpair)
            applied_rule = True

    if applied_rule:
        continue


    # Apply Rule 3. If the letters appear on the same column of your
    # table, replace them with the letters immediately below
    # respectively
    for j in range(5):
        col = "".join([key_matrix[i][j] for i in range(5)])
        if pair[0] in col and pair[1] in col:
            firstpair = col.find(pair[0])
            secondpair = col.find(pair[1])

            ciphertextpair = col[(firstpair + 1)%5] + col[(secondpair + 1)%5]
            ciphertextpairs.append(ciphertextpair)
            applied_rule = True

    if applied_rule:
        continue

    # Apply Rule 4. If the letters are not on the same row or column,
    # replace them with the letters on the same row respectively but
    # at the other pair of corners of the rectangle defined by the
    # original pair
    i0 = 0
    i1 = 0
    j0 = 0
    j1 = 0

    for i in range(5):
        row = key_matrix[i]
        if pair[0] in row:
            i0 = i
            j0 = row.find(pair[0])

        if pair[1] in row:
            i1 = i
            j1 = row.find(pair[1])

    ciphertextpair = key_matrix[i0][j1] + key_matrix[i1][j0]

    ciphertextpairs.append(ciphertextpair)

print(ciphertextpairs)

print("plaintext: " + plaintext)
print("cipher   : " + "".join(ciphertextpairs))



