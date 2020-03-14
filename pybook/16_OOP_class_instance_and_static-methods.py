"""
SUMMARY:
    - INSTANCE METHODS need a class instance and can access the instance through 'self' .
    - CLASS METHODS don't need a class instance. They can't access the instance (self) but they have access to the
    class itself via 'cls' .
    - STATIC METHODS don't have access to 'cls' or 'self' .

INSTANCE METHOD:
    - The basic, no-frills method type you will use most of the time.
    - Takes at least 1 argument: 'self', through which it can access attributes and other methods on the same object.
    - This gives it a lot of power when it comes to modifying an object’s state.

CLASS METHOD:
    - This method is marked with a @classmethod decorator to flag it as a CLASS METHOD.
    - Instead of accepting a self parameter, class methods take a cls parameter that points to the class—and not
    the object instance—when the method is called.
    - Because the class method only has access to this cls argument, it can’t modify object instance state. That would
    require access to self.
    - However, class methods can still modify class state that applies across all instances of the class.

STATIC METHOD:
    - This method is marked with a @staticmethod decorator to flag it as a STATIC METHOD.
    - This type of method takes neither a self nor a cls parameter (but of course it is free to accept an arbitrary
    number of other parameters).
    - Therefore a static method can neither modify object state nor class state.
    - They are restricted in what data they can access - and they are primarily a way to namespace your methods.
    - They behave like regular methods, but we include them in our classes because they have some logical connection
    to our class.
"""

print('\n######################################### 1. SIMPLE CLASS METHOD #########################################\n')


class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    # The next 2 methods are INSTANCE METHODS
    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)                  # we could also use Employee.raise_amt here

    @classmethod    # altering our method functionality so that we now receive cls as the 1st argument instead of self
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount


emp_1 = Employee('Omar', 'Aziz', 60000)
emp_2 = Employee('Graham', 'Bell', 50000)

Employee.set_raise_amt(1.05)        # running the class method

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

print('\n########################### 2. USING CLASS METHODS AS ALTERNATIVE CONSTRUCTORS ###########################\n')
"""
Using class methods as ALTERNATIVE CONSTRUCTORS means that we can use class methods in order to provide multiple ways of
creating instances.

For instance, for the Employee class above, if someone says that they are getting employee information in the form of a 
string, with hyphens used as separators, and instead of parsing strings everytime, they want to directly pass in the 
string (to a method) and have the employee instances created from that. This is a case where we can use a class method 
as an ALTERNATIVE CONSTRUCTOR.  
"""


class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)               # we could also use Employee.raise_amt here

    @classmethod    # altering our method functionality so that we now receive cls as the 1st argument instead of self
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    # CLASS METHOD ALTERNATIVE CONSTRUCTOR
    @classmethod
    def from_string(cls, emp_str):                              # by convention, constructor names start with 'from'
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)                            # remember to return the Employee object


# Employee strings
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Paul-Jackson-90000'

# Using the CLASS METHOD ALTERNATIVE CONSTRUCTOR to create employee instances from strings
new_emp_1 = Employee.from_string(emp_str_1)
new_emp_2 = Employee.from_string(emp_str_2)
new_emp_3 = Employee.from_string(emp_str_3)

print(new_emp_1)                        # printing employee object and its location on memory
print(new_emp_1.email)
print(new_emp_1.pay)
print()
print(new_emp_2)                        # printing employee object and its location on memory
print(new_emp_2.email)
print(new_emp_2.pay)
print()
print(new_emp_3)                        # printing employee object and its location on memory
print(new_emp_3.email)
print(new_emp_3.pay)

print('\n######################################## 3. STATIC METHOD EXAMPLE ########################################\n')
"""
STATIC METHODS take neither the instance (self), nor the class (cls) as an argument. They behave like regular methods, 
but we include them in our classes because they have some logical connection to our class.
"""


class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)                  # we could also use Employee.raise_amt here

    @classmethod    # altering our method functionality so that we now receive cls as the 1st argument instead of self
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    # CLASS METHOD ALTERNATIVE CONSTRUCTOR
    @classmethod
    def from_string(cls, emp_str):                              # by convention, constructor names start with 'from'
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)                            # remember to return the Employee object

    # Static method. This method checks whether a particular date is a weekday or a weekend.
    @staticmethod
    def is_workday(day):
        if day.weekday == 5 or day.weekday == 6:                    # 0 = Monday, 5 = Saturday, and 6 = Sunday
            return False
        return True


import datetime
my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))


