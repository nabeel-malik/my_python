"""
INHERITANCE allows us to define a class that inherits all the methods and properties from another class.
    Base class is the class being inherited from, also called parent class.
    Derived class is the class that inherits from another class, also called child class.
    We can redefine base class methods inside a derived class by simply re-writing them using the same method name.
"""


class Animal():                         # BASE CLASS
    def __init__(self):
        print('ANIMAL CREATED')

    def who_am_i(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')


class Dog(Animal):                      # DERIVED CLASS inheriting from the BASE CLASS
    def __init__(self):
        Animal.__init__(self)       # Creating an instance of Animal() class when an instance of Dog() class is created.
        print('DOG CREATED')

    def who_am_i(self):                 # Redefining a method inherited from BASE CLASS
        print('I am a dog')


mydog = Dog()           # Creating an instance of the class Dog() called mydog
mydog.who_am_i()
mydog.eat()

