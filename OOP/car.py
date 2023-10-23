# Classnames should be capital as a common naming convention

class Car:

    # Attribute
    # - Describe what an object is
    # Wheels = 4

    # Class variables
    # Is data shared among all classes

    Wheels = 4

    # Constructor/Initializer

    def __init__(self, make, model, year, color):
        # Instance variables are variables declared inside the constructor
        # affects only the instance
        print(self.make)
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    # Methods
    # What the object can perform/do
    def drive(self):
        print('This car is driving a ' + self.model)

    def stop(self):
        print("This car is stopped")
