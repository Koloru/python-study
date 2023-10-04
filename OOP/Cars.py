from car import Car


ferrari = Car(make="Ferrari", model="f40", color="red", year=2021)

# 4
print(ferrari.Wheels)

# Affects all instances of a class
Car.Wheels = 0

# 0
print(ferrari.Wheels)
