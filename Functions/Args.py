
# Args allow you to pass multiple non-key arguments
# or if you want to pass an X number of args for example adding an X amount of numbers
# you can use the * "unpacking operator"
# works the same as destructuring in javascript


def add_numbers(*nums):
    total = 0
    for num in nums:
        total += num
    return total


array = [1, 2, 3, 4, 5, 6]

print(array)
