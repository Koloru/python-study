import os
import shutil

# path = 'empty'

# try:
    # does not remove empty folders
    # os.remove(path)
    # removes empty folders
    # os.rmdir(path)
    # delete folders that contain files
    # be careful with this because it delets everything in a directory alongside the directory
    # shutil.rmtree(path)
# except Exception as e:
#     print(e)



number = int(input("Enter a number: "))

if number % 2 == 0:
  print('Event Number')
else:
  print('Odd Number')