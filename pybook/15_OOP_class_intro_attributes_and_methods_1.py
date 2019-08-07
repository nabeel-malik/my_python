class Dog():
    """
    There are 2 kinds of attributes: Class object attributes, and user-defined attributes.
    Class object attributes are common to each and every instance of the class. They are defined above '__init__'.
    User-defined attributes are specific to each instance of the class. They are defined inside __init__'

    '__init__' is a special method that is called whenever Python creates a new instance of the class (Instantiation).
    The first parameter 'self' is mandatory, and just refers to that particular instance of the class.
    By convention, the arguments passed to the '__init__' method have the same name as the user-defined attributes.
    """

    species = 'mammal'                  # 'mammal' assigned to CLASS OBJECT ATTRIBUTE called 'species'

    def __init__(self, breed, name, spots):          # INSTANTIATION METHOD

        # Expecting string
        self.breed = breed              # breed parameter assigned to USER-DEFINED ATTRIBUTE called 'breed'
        self.name = name

        # Expecting boolean
        self.spots = spots

    def bark(self, mood):                     # CLASS METHOD called bark()
        mood = mood.title()
        print('{0} WOOF! from {1}'.format(mood, self.name))     # Notice how 'mood' parameter is not linked to 'self'


my_dog = Dog('Huskie', 'Oscar', False)      # Creating an instance of the class Dog() called my_dog

print('########## Printing instance type ##########')
print(type(my_dog), '\n')

print('########## Printing attributes ##########')
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots, '\n')

print('########## Running class method ##########')
my_dog.bark('angry')            # Note: Attribute call has no () at the end, but method call does.
