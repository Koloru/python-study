
# and, or, not are the three logical operators


# and operator
age = 37

if age >= 18 and age <= 50:
  print('You are not a senior citizen')
elif age > 50:
  print('You are a senior citizen')
elif age > 0 and age < 18:
  print('you are a minor')
else:
  print('you are not yet born')
  

# or and not operator
canadian = False
if canadian == 'citizen' or 'canadian student':
  print('You are currently in canada')
else:
  print('you are not in canada')
  
if not canadian:
  print('yo')