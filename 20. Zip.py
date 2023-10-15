# Combines 2 or more iterable elements
# Lists, Tuples, Sets, etc
# Creates a zip object with paired elements from each iterable

usernames = ["a", "b", "c"]
password = [1, 2, 3, 4, 5]


new = zip(usernames, password)


for i in new:
    print(i)

    # ('a', 1)
    # ('b', 2)
    # ('c', 3)
