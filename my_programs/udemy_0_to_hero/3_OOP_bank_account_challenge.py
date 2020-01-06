class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        print("New account successfully opened!\n")

    # String to return when print() function is called on an object of the class 'Account'
    def __str__(self):
        return "Account owner:\t\t{0}\nAccount balance:\t{1}\n".format(self.owner, self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Deposit of {0} successful!".format(amount))
        print("Account owner:\t\t{0}\nAccount balance:\t{1}\n".format(self.owner, self.balance))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!\n")
        else:
            self.balance -= amount
            print("Withdrawal of {0} successful!".format(amount))
            print("Account owner:\t\t{0}\nAccount balance:\t{1}\n".format(self.owner, self.balance))


account1 = Account("Jose", 200)
print(account1)         # print() call on object
account1.deposit(500)
account1.withdraw(1000)
account1.withdraw(300)

