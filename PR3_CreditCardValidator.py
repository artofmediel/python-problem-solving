# Python credit card validator program

# 1. Remove any '-' or ' '
# 2. Add all digits in the odd places from right to left
# 3. Double every second digit from right to left
#       (if the result is a 2-digit number,
#       add the 2-digit number together to get a single digit.)
# 4. Sum the totals of steps 2 & 3
# 5. If sum is divisible by 10, the credit card# is valid

sum_odd_digits = 0
sum_even_digits= 0
total = 0

# step 1
card_number = input("Enter a credit card #: ")
card_number = card_number.replace("-","")
card_number = card_number.replace(" ", "")
# check
#print(card_number)
# reverse the string
card_number = card_number[::-1]

# step 2
# iterate every 2nd digit on the card_number
for x in card_number[::2]:
    sum_odd_digits += int(x)    # cast x from string to int

# step 3
for x in card_number[1::2]:
    x = int(x) * 2
    # check if x is a 2-digit number
    if x >= 10:
        sum_even_digits += (1 + (x % 10))
        # example:
        # 9x2 = 18
        # 18%2 = 8
        # 8+1 = 9
    else:
        sum_even_digits += x

# step 4
total = sum_odd_digits + sum_even_digits

# step 5
if total % 10 == 0:
    print("VALID")
else:
    print("INVALID")

# sample of valid numbers found online
#
# Test Credit Card Account Numbers
# American Express 378282246310005
# American Express 371449635398431
# American Express Corporate 378734493671000
# Australian Bankcard 5610591081018250
# Diners Club 30569309025904
# Diners Club 38520000023237
# Discover 6011111111111117
# Discover 6011000990139424
# JCB 3530111333300000
# JCB 3566002020360505
# MasterCard 5555555555554444
# MasterCard 5105105105105100
# Visa 4111111111111111
# Visa 4012888888881881