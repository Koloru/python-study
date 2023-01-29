
# Python credit card validator program

# 1. Remove any '-' or ' '
# 2. Add all digits in the odd places from right to left
# 3. Double every second digit from right to left.
#        (If result is a two-digit number,
#        add the two-digit number together to get a single digit.)
# 4. Sum the totals of steps 2 & 3
# 5. If sum is divisible by 10, the credit card # is valid

sum_odd_digits = 0
sum_even_digits = 0
total = 0

card_number = "378282246310005"
exp_date = "5/2029"
cvc = "187"

# Format Credit Card Number to remove -
card_number = card_number.replace("-", "")
card_number = card_number.replace(" ", "")

# Reverse card number / Reverse String
card_number = card_number[::-1]

# add all digits in tge odd places from right to left
for x in card_number[::2]:
    sum_odd_digits += int(x)
    # Step 2

# Double every second digit from right to left
for x in card_number[1::2]:
    x = int(x)*2
    # If result is a two-digit number,
    # add the two-digit number together to get a single digit.
    if x >= 10:
        sum_even_digits += (1 + (x % 10))
    else:
        sum_even_digits += x
        

# Sum the totals of steps 2 & 3
total = sum_even_digits + sum_odd_digits


# 5. If sum is divisible by 10, the credit card # is valid
if total % 10 == 0:
    print("Valid card number")
else:
    print("Invalid card number")
