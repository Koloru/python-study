# Lambdas are mainly one line functions that take parameters and return an operation/expression
# mainly works the same as an anonymouse function in javascript
# Syntax
# lambda param1, param2: expression
# ex:
# lambda add_two first, second: first + second
# add_two = lambda x,y : x+y
def add_two(x, y):
    return x+y


print(add_two(2, 2))


# When to use Lambda

# Making a function builder with lambda
# Function takes in an x parameter and returns a function that takes in a number

def func_builder(x):
    return lambda num: num + x


add_ten = func_builder(2)
print(add_ten(10))  # 20

add_three = func_builder(3)
print(add_three(10))
