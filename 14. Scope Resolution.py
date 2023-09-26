# Python Scope Resolution
# L = Local - Inside a function
# E = Enclosed - inside functions of functions?
# G = Global - Global Variables
# B = Built-in - Inside libraries
# L -> E -> G -> B
# Variable Scope
# Variable a is local to function1 and can only be accessed within function1
def func1():
    a = 1
    print(a)
