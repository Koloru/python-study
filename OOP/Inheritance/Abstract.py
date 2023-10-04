# Abstract classes prevent a user from creating an object of that class
# compels a user to override methods in a child class

from abc import ABC, abstractmethod


# the vehicle object is now prevented from being created
class Vehicle(ABC):
    '''creates a vehicle class'''
    @abstractmethod
    # Go is supposed to be overriden by the user
    # so we turn it into an abstract method
    # abstract classes should have 1 abstract method for them to be astract
    # children classes also need to implement abstractmethods for them to not
    # have any type errors
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


# Because Car does not have the stop method it will provide the following error
# TypeError: Can't instantiate abstract class Car with abstract method stop
class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("this car stopped")


class Motorcycle(Vehicle):
    def go(self):
        print('Motorcycle is driving')

    def stop(self):
        print("stopping the Motorcycle")
