"""
SPECIAL/DUNDER METHODS are a set of predefined methods you can use to enrich your classes. They are easy to
recognize because they start and end with "double underscores" (hence 'DUNDER'), for example __init__ OR __str__.

SPECIAL/DUNDER METHODS let you emulate the behavior of built-in types that an empty class definition does not
support by default.
"""


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # print() function just displays the string representation [str() function] of the given object.
    def __str__(self):
        return "{0} by {1}".format(self.title, self.author)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A Book object has been deleted.")


mybook = Book('Python rocks', 'Jose', 200)


print(mybook)           # The print() function will now look for the __str__() DUNDER METHOD in the class 'Book'.
print(len(mybook))      # The len() function will now look for the __len__() DUNDER METHOD in the class 'Book'.
del mybook              # del function is used to delete instances of classes.

"""
Look at X_OOP_blackjack_game & X_OOP_bank_account_challenge in 'udemy_0_to_hero' directory for challenge problems 
combining a lot of the OOP concepts from pybook.
"""