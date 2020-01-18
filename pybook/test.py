class Employee:

    def __init__(self, first, last):
        self.__first = first                                      # note: all attributes are private here
        self.__last = last
        self.__fullname = first + ' ' + last                      # will run the 'fullname' setter method below
        self.__email = first + '.' + last + '@email.com'          # will run the 'email' setter method below
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

emp1.first = 'Jim'              # note: we are accessing the first property here, not the '__first' private variable
print(emp1.details)

emp1.fullname = 'Bob Cole'
print(emp1.details)