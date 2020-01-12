"""
An ABSTRACT CLASS is a class that you would never expect to instantiate, but would serve as a PARENT CLASS to a
subclass (CHILD CLASS) that you would expect to instantiate.

Method names that you would expect to be common in all the CHILD CLASSES of a PARENT CLASS (which in this case in an
ABSTRACT CLASS), can pe placed in the ABSTRACT CLASS with the RAISE method to raise an error if this method is called
on an instance of the ABSTRACT CLASS, instead of being called on an instance of one of the CHILD CLASSES.

This approach is more commonly used to utilize POLYMORPHISM, i.e. when a method name is to be shared across a number of
classes.
"""

# ABSTRACT, PARENT CLASS
class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

# CHILD CLASS
class Dog(Animal):

    def speak(self):
        print(self.name + " says WOOF!")

# CHILD CLASS
class Cat(Animal):

    def speak(self):
        print(self.name + " says MEOW!")

# INSTANTIATING THE ANIMAL CLASS (ABSTRACT, PARENT CLASS) AND CALLING speak() METHOD WILL RAISE THE NotImplementedError
# myanimal = Animal("Fred")
# myanimal.speak()


# INSTANTIATING THE DOG CLASS (CHILD CLASS) AND CALLING speak() METHOD
mydog = Dog("Max")
mydog.speak()

# INSTANTIATING THE CAT CLASS (CHILD CLASS) AND CALLING speak() METHOD
mycat = Cat("Leo")
mycat.speak()


