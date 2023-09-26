# Defining a function

def function_name():
    print("Hello World")


# Invoking a function
function_name()


def call_name(age, name='eh'):
    return print(f'yo {name} {age}')


# If you want to mix up the order of the parameters you can name them when passing into the function
call_name(name="neil", age=25)
