"""
INHERITANCE allows us to define a class that inherits all the methods and properties from another class.
    'Parent class' is the class being inherited from.
    'Child class' is the class that inherits from the 'parent class'.
    We can redefine parent class methods inside a child class by simply re-writing them using the same method name.
    We can also add more methods specific to the child class.
"""


class Animal:                       # PARENT CLASS
    def __init__(self):
        print('ANIMAL CREATED')

    def who_am_i(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')


class Dog(Animal):                  # CHILD CLASS inheriting from the BASE CLASS
    def __init__(self):
        Animal.__init__(self)       # Creating an instance of Animal() class when an instance of Dog() class is created.
        print('DOG CREATED')

    def who_am_i(self):             # 'Over-writing' a method inherited from PARENT CLASS, aka METHOD OVERRIDING.
        print('I am a dog')

    def bark(self):                 # Adding a method to the methods inherited from the PARENT CLASS
        print('WOOF!')


mydog = Dog()                       # Creating an instance of the class Dog() called mydog

mydog.who_am_i()
mydog.eat()
mydog.bark()

