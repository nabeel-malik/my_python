'''
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
    - This type of method takes neither a self nor a cls parameter (but of course it’s free to accept an arbitrary
    number of other parameters).
    - Therefore a static method can neither modify object state nor class state.
    - They are restricted in what data they can access - and they are primarily a way to namespace your methods.
'''


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
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)                  # we could also use Employee.raise_amt here

    @classmethod    # altering our method functionality so that we now receive cls as the 1st argument instead of self
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount


emp_1 = Employee('Omar', 'Aziz', 60000)
emp_2 = Employee('Graham', 'Bell', 50000)

Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

