class BankAccount:
# accepts an account name and starting balance
    def __init__(self, account_name, starting_balance):
        self.account_name = account_name
        self.balance = starting_balance
# addes funds to the account
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
# withdraw funds from the accoubnt
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
# to get and print the account balance
    def get_balance(self):
        return f"{self.account_name} has a balance of {self.balance}"

my_account = BankAccount("Wally", 50) 
my_account.deposit(51) 
my_account.withdraw(30.86) 

print(my_account.get_balance())
