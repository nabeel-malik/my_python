"""
POLYMORPHISM refers to the way in which different object classes can share the same method name, and then those
methods can be called from the same place (for instance, a loop or function) even though a variety of different
objects might be passed in.
"""

class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' says WOOF!')


class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' says MEOW!')


bruno = Dog('Bruno')        # Creating an instance of the Dog class
felix = Cat('Felix')        # Creating an instance of the Cat class

print('\n######## 1. DEMONSTRATING POLYMORPHISM BY SIMPLY CALLING THE COMMONLY NAMED METHOD SEQUENTIALLY ########\n')

bruno.speak()
felix.speak()


print('\n######## 2. DEMONSTRATING POLYMORPHISM BY CALLING THE COMMONLY NAMED METHOD USING A LOOP ########\n')

for pet in [bruno, felix]:
    print(type(pet))
    pet.speak()


print('\n######## 3. DEMONSTRATING POLYMORPHISM BY CALLING THE COMMONLY NAMED METHOD USING A FUNCTION ########\n')

def pet_speak(pet_obj):
    print(type(pet_obj))
    pet_obj.speak()

pet_speak(bruno)
pet_speak(felix)