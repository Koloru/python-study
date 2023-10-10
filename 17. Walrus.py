# Walrus operator
# :=


# Assignment operation
# Assigns values to variables as part of a larger expression
# The main purpose of the walrus operator is to both evaluate an expression
# and assign its value to a variable in a single step, especially in contexts
# where using a traditional assignment would be syntactically invalid.

# Normal assignment
# happy = True
# print(happy)


# Does not work when you create a variable as a parameter
# print(happy = True)


# basic example usage
# works because of the walrus operator because its an expression and an assignment at the same time
print(happy := True)


# Practical example

# You can rewrite this as
foods = list()


while True:
    food = input("What food do you like: ")
    if food == "quit":
        break
    foods.append(food)


# walrus operator for the most part is basically and assignment + a condition after
# you create a variable to assign to it and then compared it with a condition after it

while food := input("What food do you like? ") != "quit":
    foods.append(food)


print(foods)
