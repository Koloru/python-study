import os
import time

name = input("enter your name: ")

while name == "":
    print("You did not type anything")
    time.sleep(0.2)
    os.system('cls')
    name = input("enter your name: ")

print(f"Hello {name}")
