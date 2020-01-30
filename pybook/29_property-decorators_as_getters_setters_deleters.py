"""
In python, everything is an object. And every object has attributes, and methods or functions.
Attributes are described by data variables for example like name, age, height etc.
Properties are special kind of attributes which have getter, setter and delete methods. (See section 2)

A GETTER is a method that gets the value of an attribute. A SETTER is a method that sets the value of an attribute.
In OOPs, GETTER and SETTER methods are used for DATA ENCAPSULATION, whereby the implementation details of a class are
kept hidden from the user. The user can only perform a restricted set of operations on the hidden members of the class
by executing special functions commonly called methods.

GETTERS and SETTERS are used for the following reasons:
    - For completeness of encapsulation.
    - To maintain a consistent interface in case internal details change.
    - To add validation logic around getting and setting a value.
    - Hiding the internal representation of the property.
    - To avoid direct access or modification of a class field.
    - Getters and setters can allow different access levels.

There are 3 common ways to implement GETTER and SETTER functionality in Python:
    - Only GETTER and SETTER METHODS (section 1),
    - PROPERTY FUNCTION (section 2), or
    - @property DECORATOR (section 3)
"""

print('\n#################################### 1. ONLY GETTER AND SETTER METHODS ####################################\n')
"""
Using ONLY GETTER AND SETTER METHODS belongs to the sad world of Java/C++. In languages like Python it's unnecessary! 
You can just begin with a plain attribute, letting clients access it. If, at some point, a need will arise to hide the 
attribute from direct access, we can use the PROPERTY FUNCTION (section 2) or @property DECORATOR (section 3).
"""


class Employee:

    def __init__(self, name, company):
        self.__name = name                  # '__' before attribute names makes them private
        self.__company = company

    # GETTER METHOD
    def getcompany(self):
        print('Getter method called.')
        return self.__company

    # SETTER METHOD
    def setcompany(self, value):
        print('Setter method called.')
        self.__company = value


e = Employee('Richard', 'Google')
print('Company name:', e.getcompany(), '\n')      # notice that the public can not 'directly' access the variable

e.setcompany('Amazon')                      # notice that the public can not 'directly' access the variable
print()

print('Company name:', e.getcompany())

# print(e.__company)              # this would raise an error, since attributes that begin with '__' are private


print('\n######################################### 2. property() FUNCTION #########################################\n')
"""
In Python property()is a built-in function that creates and returns a property object. 
A property object has three methods: getter(), setter(), and delete(). 
The property() function has four arguments: 
    - fget:     is a function for retrieving an attribute value. 
    - fset:     is a function for setting an attribute value. 
    - fdel:     is a function for deleting an attribute value. 
    - doc:      creates a docstring for attribute. 

Usage:      x = property(fget, fset, fdel, doc)     where x is the name of the new property object
"""


class Employee:

    def __init__(self, name, company):
        self.__name = name                  # '__' before attribute names makes them private
        self.__company = company
        print("New instance of '{}' class created.".format(type(self).__name__), '\n')      # to print class name

    # GETTER METHOD
    def getcompany(self):
        print('Getter method called.')
        return self.__company

    # SETTER METHOD
    def setcompany(self, value):
        print('Setter method called.')
        self.__company = value

    # DELETER METHOD
    def deletecompany(self):
        del self.__company

    # The following 3 lines of code will run before the code outside the class defintion
    company = property(getcompany, setcompany, deletecompany)       # property object assigned to 'company' variable
    print("New instance of '{}' class created.".format(type(company).__name__))       # to print class name
    print(company, '\n')                # will print the property object and its location on memory


e = Employee('Bob', 'Microsoft')

print('Company name:', e.company, '\n')           # notice that the public can not directly access the variable

e.company = 'Alphabet'
print()

print('Company name:', e.company)

# print(e.__company)              # this would raise an error, since attributes that begin with '__' are private


print('\n################################### 3. @property DECORATOR - EXAMPLE 1 ###################################\n')
"""
There is one more way to implement property() function i.e. by using decorators. 
Python @property is one of the built-in decorators. The main purpose of any decorator is to change your class methods 
or attributes in such a way so that the user of your class does not need to make any change in their code.

'The @property decorator allows us to define a method, but we can access it like an attribute' - Corey Schafer.
"""


class Employee:

    def __init__(self, name, company):
        self.__name = name                  # '__' before attribute names makes them private
        self.__company = company
        print("New instance of '{}' class created.".format(type(self).__name__), '\n')      # to print class name

    @property
    def name(self):
        print('Getter method called.')
        return self.__name

    @property
    def company(self):
        print('Getter method called.')
        return self.__company

    @name.setter
    def name(self, value):
        print('Setter method called.')
        self.__name = value

    @company.setter
    def company(self, value):
        print('Setter method called.')
        self.__company = value


emp_1 = Employee('Marco', 'Shell')

print('Company name:', emp_1.company, '\n')           # notice that the public can not directly access the variable

emp_1.company = 'Exxon Mobil'
print()

print('Company name:', emp_1.company)

# print(emp_1.__company)              # this would raise an error, since private attributes are not publicly accessible

print('\n################################### 4. @property DECORATOR - EXAMPLE 2 ###################################\n')
"""
In this example, ALL INSTANCE ATTRIBUTES ARE PUBLIC, and there are 2 base attributes, and 2 derived attributes.
In such a case, we would define separate getter and setter functions and decorators for the DERIVED attributes (because,
in case the base attributes are publicly modified, the __init__ method will not rerun to derive these attributes again) 
In the following example, fullname and email are the derived attributes.
"""


class Employee:

    def __init__(self, first, last):
        self.first = first                                      # note: all attributes are public here
        self.last = last
        self.fullname = first + ' ' + last                      # will run the 'fullname' setter method below
        self.email = first + '.' + last + '@email.com'          # will run the 'email' setter method below
        print("New instance of '{}' class created.".format(type(self).__name__))

    # GETTER METHODS FOR DERIVED ATTRIBUTES
    @property
    def fullname(self):
        return self.first + ' ' + self.last

    @property
    def email(self):
        return self.first + '.' + self.last + '@email.com'

    # SETTER METHODS FOR DERIVED ATTRIBUTES
    @fullname.setter
    def fullname(self, value):
        self.first, self.last = value.split(' ')

    @email.setter
    def email(self, value):
        self.first, self.last = value.split('@')[0].split('.')

    # GETTER METHOD FOR DETAILS
    @property
    def details(self):
        return '''First name:\t\t{}\nFull name:\t\t{}\nEmail:\t\t\t{}\n'''.format(self.first, self.fullname, self.email)
        # note: the return statement above will run the getter methods and decorators for fullname and email.


emp1 = Employee('John', 'Smith')
print(emp1.details)

emp1.first = 'Jim'              # note: 'first' is a public variable and can be accessed directly
print(emp1.details)

emp1.fullname = 'Bob Cole'      # note that although 'fullname' is a function, it can be accessed like an attribute
print(emp1.details)


print('\n################################### 5. @property DECORATOR - EXAMPLE 3 ###################################\n')
"""
This is the same as EXAMPLE 2, except that ALL INSTANCE ATTRIBUTES ARE PRIVATE, and hence not publicly accessible. 
This means that we would now create getter and setter functions and decorators for ALL the attributes, since none of 
them would be directly accessible publicly.
"""


class Employee:

    def __init__(self, first, last):
        self.__first = first                                      # note: all attributes are private here
        self.__last = last
        self.__fullname = first + ' ' + last
        self.__email = first + '.' + last + '@email.com'
        print("New instance of '{}' class created.".format(type(self).__name__))

    # GETTER METHODS FOR ALL PRIVATE ATTRIBUTES
    @property
    def first(self):
        return self.__first

    @property
    def last(self):
        return self.__last

    @property
    def fullname(self):
        return self.__first + ' ' + self.__last

    @property
    def email(self):
        return self.__first + '.' + self.__last + '@email.com'

    # SETTER METHODS FOR ALL PRIVATE ATTRIBUTES
    @first.setter
    def first(self, value):
        self.__first = value

    @last.setter
    def last(self, value):
        self.__last = value

    @fullname.setter
    def fullname(self, value):
        self.__first, self.__last = value.split(' ')

    @email.setter
    def email(self, value):
        self.__first, self.__last = value.split('@')[0].split('.')

    # GETTER METHOD FOR DETAILS
    @property
    def details(self):
        return 'First name:\t\t{}\nFull name:\t\t{}\nEmail:\t\t\t{}\n'.format(self.first, self.fullname, self.email)
        # note: the return statement above will run the getter methods and decorators for first, fullname and email.


emp1 = Employee('John', 'Smith')
print(emp1.details)

emp1.first = 'Jim'              # note: we are accessing the 'first' property here, not the '__first' private variable
print(emp1.details)

emp1.fullname = 'Bob Cole'
print(emp1.details)