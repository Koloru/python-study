
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


for x in card_number[::2]:
    sum_odd_digits += int(x)
    # Step 2

for x in card_number[1::2]:
    x = int(x)*2
    if x >= 10:
        sum_even_digits += (1 + (x % 10))
    else:
        sum_even_digits += x
        


total = sum_even_digits + sum_odd_digits

if total % 10 == 0:
    print("Valid card number")
else:
    print("Invalid card number")
