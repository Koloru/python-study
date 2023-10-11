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

# The if conditional is optional
# list_name = [(expression/condition) for ITEM in ITERABLE if conditional]
squares = [add(i) for i in range(1, 11) ]

# Add it to the last if i is greater than 2
squares = [(i+i) for i in range(1, 11) if i > 2]
print(squares)

# adding more than 1 conditional the formula syntax changes
# it turns into
# list_name = [(expression/condition) (if/else) for ITEM in ITERABLE]

# Read as add i+i if i is greater than 2 else make it failed in the range of 1,11
squares = [(i+i) if i > 2 else "failed" for i in range(1, 11) ]
print(squares)

# Using list comprehension to mimic lambda functions
