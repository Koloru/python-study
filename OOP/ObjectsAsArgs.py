class Car:
    color = None


class Motorcycle:
    color = None


def change_color(car: Car, color):
    car.color = color


car1 = Car()
car2 = Car()
car3 = Car()

change_color(car1, 'red')
change_color(car2, 'yellow')
change_color(car3, 'black')

print(car1.color)
print(car2.color)
print(car3.color)


bike1 = Motorcycle()

change_color(bike1, 'Cyan')

print(bike1.color)
