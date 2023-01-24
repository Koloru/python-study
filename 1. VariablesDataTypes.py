
name = "John Doe"
age = 25
employed = True
netWorth = 42.99

print(type(name))
print(type(age))
print(type(employed))
print(type(netWorth))

# template literal / printing strings
print(f"hi {name}, you are {age} and you are currently {employed}")

print("hi "+str(name)+ ", you are "+str(age)+" and you are currently "+str(employed))
print("hi ",name,", you are ",age," and you are currently ", employed)

# Tips and Tricks
# You can assign variables like this
x, y, z = 1, 2, "40"


# a,b and c are all assigned to 0
a = b = c = 0