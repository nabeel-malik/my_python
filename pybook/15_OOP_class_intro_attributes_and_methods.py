"""
There are 2 kinds of attributes: CLASS ATTRIBUTES, and INSTANCE ATTRIBUTES.
'CLASS ATTRIBUTES' are common to ALL instances of the class. They are defined above '__init__'.
'INSTANCE ATTRIBUTES' are specific to particular instances of the class. They are defined inside __init__'.
Any function defined 'inside' a class is called a 'METHOD'.

'__init__' is a special method that is called whenever Python creates a new instance of the class (Instantiation).
The first parameter 'self' is mandatory, and just refers to that particular instance of the class.
By convention, the argument names in the '__init__' method definition are the same as the instance attributes.
"""

print('\n##################################### 1. CLASS EXAMPLE 1 - DOG CLASS #####################################\n')


class Dog:    # The class keyword creates user-defined objects, as opposed to built-in objects like strings and lists.

    species = 'Mammal'                  # 'Mammal' assigned to CLASS ATTRIBUTE called 'species'

    def __init__(self, breed, name, spots):          # INSTANTIATION METHOD, aka INIT METHOD

        # Expecting string
        self.breed = breed              # breed argument assigned to INSTANCE ATTRIBUTE called 'breed'
        self.name = name

        # Expecting boolean
        self.spots = spots

    def bark(self, mood):                     # INSTANCE METHOD called bark()
        mood = mood.title()
        print(f'{mood} WOOF! from {self.name}')     # Notice how 'mood' parameter is not linked to 'self'


my_dog = Dog('Huskie', 'Oscar', False)      # Creating an instance of the class Dog() called my_dog

print('---------- Printing instance type ----------')
print(type(my_dog), '\n')

print('---------- Printing attributes ----------')

print(my_dog.species)       # Printing 'CLASS ATTRIBUTE' that is common to ALL instances of the class Dog()
print(my_dog.breed)         # Printing 'INSTANCE ATTRIBUTE' that is specific ONLY to the instance my_dog
print(my_dog.name)          # Printing 'INSTANCE ATTRIBUTE' that is specific ONLY to the instance my_dog
print(my_dog.spots, '\n')   # Printing 'INSTANCE ATTRIBUTE' that is specific ONLY to the instance my_dog

print('---------- Running class method ----------')
my_dog.bark('angry')            # Note: Attribute call has no () at the end, but method call does.


print('\n#################################### 2. CLASS EXAMPLE 2 - CIRCLE CLASS ####################################\n')


class Circle:

    # CLASS ATTRIBUTE
    pi = 3.142

    # INSTANTIATION/INIT METHOD
    def __init__(self, radius=1):           # Can set default values for parameters just like regular functions.
        # INSTANCE ATTRIBUTES
        self.radius = radius
        self.area = Circle.pi * self.radius * self.radius       # We can create additional attributes inside '__init__'

    # INSTANCE METHOD
    def get_circumference(self):
        return 2 * Circle.pi * self.radius       # We can use both 'Circle.pi' or 'self.pi'. 'Circle.pi' is preferred.


my_circle = Circle(5)      # Creating and instance of the class Circle(). This is where 'area' attribute is calculated.

print('---------- Printing CLASS ATTRIBUTE ----------')
print(my_circle.pi, '\n')

print('---------- Printing INSTANCE ATTRIBUTES ----------')
my_circle.radius = 10    # Reassigning a new value to the 'radius' attribute will NOT recalculate 'area' attribute.
print(my_circle.radius)
print(my_circle.area, '\n')

print('---------- Printing INSTANCE METHOD return ----------')
print(my_circle.get_circumference())
