class Circle:

    # CLASS ATTRIBUTE
    pi = 3.142

    # INSTANTIATION/INIT METHOD
    def __init__(self, radius=1):           # Can set default values for parameters just like regular functions.
        # INSTANCE ATTRIBUTES
        self.radius = radius
        self.area = Circle.pi * self.radius * self.radius       # We can create additional attributes inside '__init__'

    # CLASS METHOD
    def get_circumference(self):
        return 2 * Circle.pi * self.radius       # We can use both 'Circle.pi' or 'self.pi'. 'Circle.pi' is preferred.


my_circle = Circle(5)      # Creating and instance of the class Circle(). This is where 'area' attribute is calculated.

print('########## Printing CLASS ATTRIBUTE ##########')
print(my_circle.pi,'\n')

print('########## Printing INSTANCE ATTRIBUTES ##########')
my_circle.radius = 10    # Reassigning a new value to the 'radius' attribute will NOT recalculate 'area' attribute.
print(my_circle.radius)
print(my_circle.area,'\n')

print('########## Printing CLASS METHOD return ##########')
print(my_circle.get_circumference())
