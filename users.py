#import BankAccount
class BankAccount:
    all_accounts = []

    def __init__(self, interest_rate=0, balance=0):
        self.balance = balance
        self.interest_rate = interest_rate
        self.__class__.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}, Interest Rate: {self.interest_rate * 100}%")
        return self

    def yield_interest(self):
        self.balance += self.balance * self.interest_rate
        return self

    @classmethod
    def display_all_accounts_info(cls):
        for account in cls.all_accounts:
            account.display_account_info()
class User:
    

    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
        
    
    def greeting(self):
        print(f"Hello My name is {self.name}")
        
    # other methods
    def make_deposit(self, amount):
    	self.account_balance += amount	# hmmm...the User class doesn't have an account_balance attribute anymore


"""  def example_method(self):
        self.account.deposit(100)		# we can call the BankAccount instance's methods
    	  print(self.account.balance)		# or access its attributes
"""
adel = User("Adel Khedhiri","khedhiri.adel@gmail.com")