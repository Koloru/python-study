#Format Specifiers
# Used to format values inside an f string by using a colon(:) after the value inside the {}
# ex: {value:formatSpecifier}

# Format specifiers also work like regex in a way you can combine them if you want to
# ex: {value:^,10}

weekly_salary = 300.1452
daily_salary = 120.13
monthly_salary = -1200.987

# Only use 2 decimal places after the whole number
# The code below will only display 2 decimal places
print(f"Your weekly salary is {weekly_salary:.2f}")

# Adding spaces before the value
# This will add 10 spaces after $
print(f"Your daily salary is ${daily_salary:10}")
# if you add a 0 before the 10 the spaces will be seeded with zeroes
print(f"Your daily salary is ${daily_salary:010},ZERO SEEDED")
# left justify / right justify(right is default)
print(f"Your daily salary is ${daily_salary:<10},Left Justified")
# center align
print(f"Your daily salary is ${daily_salary:^10},Center Aligned")


# Integers
# if you want to display the - or + in a positive or negative value all you need to do
# is add a - or + after the : you can also just use a space for positive values
print(f"Your monthly salary is {monthly_salary:}")

# thousands separator
yearly_salary = 2312351231231

print(f"your yearly salary is {yearly_salary:,}")
