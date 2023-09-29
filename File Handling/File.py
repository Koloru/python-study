import os
import random

# path = "./folder/"
path = './test.txt'


# if os.path.exists(path):
#     if os.path.isfile(path):
#         print(path)
#     elif os.path.isdir(path):
#         print('that is a directory')
# else:
#     print('doesn\'t exist.')

# reading a file
# This does not catch errors/exception
# add it to a try block to catch
# with open(path) as file:
#   print(file.read())


# Writing to a file
# the 2nd argument is for the open mode r is for read w is for write
# a for appending to the end of a file
# x for create
# t for text (default)
# b for binary
text = 'hello there'
folderDirectory = 'textfiles'


if not os.path.isdir(folderDirectory):
    os.makedirs(folderDirectory)


x = 0
while x <= 10:
    fileName = random.randint(10_000, 70_000)*10000
    filtStr = f'{fileName}'
# create a random textfile in the textfiles directory file name is the range of 10,000 to 70,000 * 10,000
    with open(f'{folderDirectory}/{fileName}.txt', 'w') as file:
        file.write(filtStr)
        x += 1


# Copying files
