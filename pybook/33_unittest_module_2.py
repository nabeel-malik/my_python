class Employee:

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first                                      # note: all attributes are public here
        self.last = last
        self.pay = pay

    # GETTER METHODS FOR DERIVED ATTRIBUTES
    @property
    def fullname(self):
        return self.first + ' ' + self.last

    @property
    def email(self):
        return self.first + '.' + self.last + '@email.com'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

