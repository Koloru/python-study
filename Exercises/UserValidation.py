username = input("Enter your username: ")

errors = []

if len(username) >= 12 or len(username) < 4:
  errors.append("Username can only have 4 to 12 characters")
  
if not username.isalpha():
  errors.append("Username can only contain letters")
  
if len(errors) > 0:
  for index, error in enumerate(errors):
    print(f"{index+1}. {error}")
else:
  print(f"Your username is {username}")


