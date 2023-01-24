

operation = input("What operation do you want to perform? ADD/SUB/MUL/DIV/MOD: ")
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
result = 0
if operation == "ADD":
  result = first_number + second_number
elif operation == "SUB":
  result = first_number - second_number
elif operation == "MUL":
  result = first_number * second_number
elif operation == "DIV":
  result = float(first_number / second_number)
elif operation == "MOD":
  result = float(first_number % second_number)
else:
  print("Unknown operation")
  
print(f"the result is {result}")