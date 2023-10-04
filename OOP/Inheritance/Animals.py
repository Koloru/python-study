class Animal:
    alive = True

    def eat(self):
        print("Eating")

    def sleep(self):
        print("Sleeping")

# Inheriting from a class


class Rabbit(Animal):

    def hop(self):
        print('Hopped')


class Fish(Animal):
    def swim(self):
        print('Swimming')


class Bird(Animal):
    def fly(self):
        print("Flying")


loki = Rabbit()

loki.hop()
