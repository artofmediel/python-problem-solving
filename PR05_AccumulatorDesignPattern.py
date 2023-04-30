# Write a function accum() that accepts a string of letters
# It then iterates to each character doing the following:
# 1. It types the letter a number of times according to the
#   position of the character
# 2. It sets the first letter of every retype to capital
#   , the rest is at lower case
# 3. It is separated by "-"
#   SAMPLE OUTPUT:
# accum("abcde")
# "A-Bb-Ccc-Dddd-Eeeee"

def accum(string):

    for i in string:
        index = string.index(i)
        retype_length = index
        # type the first in capital
        print(string.upper()[index],end="")
        # retype the rest by its index
        while retype_length != 0:
            print(string.lower()[index],end="")
            # decrement loop
            retype_length -= 1

        if (index+1) < len(string):
            print("-", end="")

    print()

while True:
    input_text = input("Enter your text here (letters only) : ")
    valid_string = True

    for i in input_text:
        if i.isalpha() == False:
            valid_string = False
        else:
            valid_string = True

    if valid_string:
        accum(input_text)
    else:
        print("Invalid Input")
        break
