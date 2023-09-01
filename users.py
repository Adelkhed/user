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
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {}  # Utilisez un dictionnaire pour stocker des comptes

    def create_account(self, account_name, int_rate=0, balance=0):
        # Crée un nouveau compte et l'associe au user
        self.accounts[account_name] = BankAccount(int_rate, balance)
        return self

    def make_deposit(self, account_name, amount):
        # Effectue un dépot dans le compte spécifié
        if account_name in self.accounts:
            self.accounts[account_name].deposit(amount)
        else:
            print("Le compte spécifié n'existe pas.")
        return self

    def make_withdrawal(self, account_name, amount):
        # Effectue un retrait du compte specifié
        if account_name in self.accounts:
            self.accounts[account_name].withdraw(amount)
        else:
            print("Le compte spécifié n'existe pas.")
        return self

    def display_user_balance(self, account_name):
        # Affiche le solde du compte spécifié
        if account_name in self.accounts:
            print(f"User : {self.name}, Compte : {account_name}")
            self.accounts[account_name].display_account_info()
        else:
            print("Le compte spécifié n'existe pas.")
        return self

adel = User("Adel Khedhiri", "khedhiri.adel@gmail.com")

# Créez deux comptes pour l'utilisateur Adel
adel.create_account("Compte1", int_rate=0.02, balance=500)
adel.create_account("Compte2", int_rate=0.03, balance=1000)

# Effectuez des opération sur les comptes
adel.make_deposit("Compte1", 500)
adel.make_withdrawal("Compte2", 500)

# Affichez les soldes des compte
adel.display_user_balance("Compte1")
adel.display_user_balance("Compte2")
