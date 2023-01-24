import math


# Arithmetic
# Addition, Subtraction, Multiplication, Division and Modulus
money = 0
money = money + 1
daily_money = money - 1
weekly_money = money / 2
bi_monthly_money = money * 2
monthly_money = money % 2

# Exponent
money = money ** 2

# built-in math functions

# round a number to the nearest whole number
rounded_number = round(69.420)  # 69

# absolute value of a number
absolute_number = abs(-2)  # 2

# power function
# 10 to the power of 3
power_number = pow(10, 3)  # 1000


# max function
# largest value between the parameters
largest_number = max(1, 2, 1000, 40000)

# min function
# smallest value between the parameters
smallest_number = min(1, 2, 10, 1000, 40000)


# Stuff below needs to import math from python
# value of pi
pi = math.pi
# e
e = math.e

# square root of a number
square_root = math.sqrt(27)

# round up
round_up = math.ceil(42.69)  # 43
# round a number down
round_down = math.floor(42.69)  # 42


# Calculate the circumference of a circle

radius = float(input('enter a radius for a circle'))
c = 2*math.pi*radius
