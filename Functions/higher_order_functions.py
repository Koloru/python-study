# higher order functions
# Functions that accept a function as an argument
# or Functions that return functions


# def loud(text):
#     return text.upper()


# def quiet(text):
#     return text.lower()


# def hello(func):
#     text = func("Hello")
#     print(text)


# hello(loud)
# hello(quiet)


# ------------ 2. returns a function -------------
def divisor(x):
    def dividend(y):
        return y / x
    return dividend


# you are setting divide to divisor
divide = divisor(2)

# Shows the memory address of the function dividend
print(divide)

# you are calling dividend in here
# passing 10 as an argument
print(divide(10))
