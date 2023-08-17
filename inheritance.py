#inheritence allows one class to inherit attributes
#and methods from another class



class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "woof"
class Cow(Animal):
    def speak(self):
        return"mooooo"

class Cat(Animal):
    def speak(self):
        return"meow"
doggy=Dog("buddy")
cat=Cat("whiskers")
cow=Cow("melisa")
print(doggy.speak())
print(cat.speak())
print(cow.speak())