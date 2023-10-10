# Create a list with less syntax
# can mimic certain lambda functions



def add(i):
    return i+i

# This can be written as
squares = []
for i in range(1, 11):
    squares.append(i * i)

print(squares)

# and can also be rewritten as
# Syntax is
# list_name = [(expression/condition) for ITEM in ITERABLE]
squares = [add(i) for i in range(1, 11)]
squares = [(i+i*i) for i in range(1, 11)]

print(squares)