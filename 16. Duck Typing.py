# class of an object is less important than the methods/attributes
# class type is not checked if minimum methods/attributes are present
# You can pass an object to a function as long as it has the same methods/functions
# ex below the chicken and duck have the same methods so the chicke is a valid parameter for the person class

class Duck:
    def walk(self):
        print("this duck is walking")

    def talk(self):
        print("duck talked")


class Chicken:
    def walk(self):
        print("Walked")

    def talk(self):
        print("talked")


class Person():
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("you caught the duck")


duck = Duck()
chicken = Chicken()

me = Person()


me.catch(duck)
