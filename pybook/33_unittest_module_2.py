import requests


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

    def monthly_schedule(self, month):
        """
        This is sample method that, we are going to pretend, goes to a company's website, and pulls down the employee's
        schedule for a given month.
        """
        # The following line is the request that needs to be replaced with a 'mock' object.
        response = requests.get(f'http://company.com/{self.last}/{month}')
        # If the response is ok, we want to return the text of that response
        if response.ok:
            return response.text
        # If the response is NOT ok, we want to return the text string 'Bad response!'
        else:
            return 'Bad response!'

