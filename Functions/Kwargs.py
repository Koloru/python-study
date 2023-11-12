# Kwarts allow you to pass keyword arguments or dicts with the unpacking operator
# but you have to use **(two asterisks)


def print_address(**kwargs):
  # kwargs is an object and you can use any object method in it
    for value in kwargs.values():
        print(value)


print_address(street="michigan", city="blaire", house=12, building="micron")
