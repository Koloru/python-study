# same with list comprehension you can make dicts with the same pattern
# can also replace loops and certain lambda functions


# dictionary = {key: expression for (key,value) in iterable}

cities = {
    'new york': 32,
    'boston': 14,
    'los angeles': 100,
    'chicago': 55
}


# The key's value is going to be the formula in the list specified after
# is how you read it
cities_new = {key: ((value - 32)*(5/9)) for (key, value) in cities.items()}


# Adding a conditional if
# will only add to the dict if the value is also less than 50
cities_cold = {
    key: ((value - 32)*(5/9)) for (key, value) in cities.items() if value < 50
}


# adding an if/else
cities_hot = {
    key: ((value - 32)*(5/9))
    if value < 50 else 'hot'
    for (key, value) in cities.items()
}

print(cities_hot)
