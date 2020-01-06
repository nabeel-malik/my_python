class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
         return "You have now opened a new account for {0} with a balance of {1}".format(self.owner, self.balance)

acct1 = Account("Jose", 200)
print(acct1)