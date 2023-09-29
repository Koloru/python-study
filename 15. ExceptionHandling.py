# exception = event detected during excecution that interrupts the normal flow of the program

try:
    numerator = int(input("enter a numerator: "))
    denominator = int(input("enter a denominator: "))
    result = numerator / denominator
# Catch exceptions with this but this  is not good practice
# its better to add more than one
# its good practice to catch specific exceptions
# Error types can be found in the error logs when you encounter one i.e. dividing by zero, dividing with strings or not putting anything
except ZeroDivisionError as e:
    print(f"you cannot divide by zero. {e}")
except ValueError as e:
    print(f"you can only divide with integer numbers. {e}")
except Exception as e:
    print(f"Something went wrong: {e}")

# If there are no exceptions execute this else statement
else:
    print(result)
# Exception or not will still get executed
finally:
    print('This will always execute at the end ')
