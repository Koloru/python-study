import os


source = 'test.text'

newDirectory = 'copied/'

if not os.path.isdir(newDirectory):
    os.makedirs(newDirectory)
    print('directory created')
else:
    print('directory already exists')

destination = newDirectory


# Moving 1 file
try:
    if os.path.exists(newDirectory+source):
        print('File already exists')
    else:
        os.replace(source, newDirectory+source)
except FileNotFoundError:
    print('file not found')


source = 'src'

# Moving a directory
try:
    if os.path.exists(newDirectory+source):
        print('File already exists')
    else:
        os.replace(source, newDirectory+source)
except FileNotFoundError:
    print('file not found')