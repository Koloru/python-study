
# Library for file based operations
import os

# Library for copying files
import shutil

# Get all files in a directory
directory = 'textfiles/'
newDirectory = 'copied/'


if not os.path.isdir(newDirectory):
    os.makedirs(newDirectory)
    print('directory created')
else:
    print('directory already exists')

files = os.listdir(directory)

for file in files:
    # copy2 preserves the folder and the metadata of a file
    # timestamps, size e.g.
    # Check https://stackoverflow.com/questions/123198/how-to-copy-files
    # copy 2 can also be a directory
    shutil.copy2(directory+file, newDirectory)
    # copy can recreate the folder if it exists as a directory
    # be careful when using copy
    # shutil.copy(directory+file, newDirectory+file)
    print(f'Moving {file} to {newDirectory}/{file}')
