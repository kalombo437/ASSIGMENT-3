class BankAccount:
    # Class variable
    interest_rate = 0.05

    # Constructor (__init__) to initialize account holder and balance
    def __init__(self, account_holder):
        self.account_holder = account_holder  # Instance variable
        self.balance = 0  # Instance variable, initial balance set to zero

    # Method to deposit money into the account
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} to {self.account_holder}'s account.")

    # Method to withdraw money from the account if funds are sufficient
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} from {self.account_holder}'s account.")
        else:
            print(f"Insufficient funds for {self.account_holder} to withdraw {amount}.")

    # Method to apply interest based on the class variable interest_rate
    def apply_interest(self):
        interest = self.balance * BankAccount.interest_rate
        self.balance += interest
        print(f"Applied interest to {self.account_holder}'s account. Interest added: {interest}")

    # Method to display the account information
    def display_account_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: {self.balance}\n")


# Task 1: Create two instances of BankAccount with different account holders
account1 = BankAccount("Alice")
account2 = BankAccount("Bob")

# Task 2: Perform deposits and withdrawals
account1.deposit(1000)
account1.withdraw(300)

account2.deposit(500)
account2.withdraw(100)

# Task 3: Apply interest using the apply_interest() method
account1.apply_interest()
account2.apply_interest()

# Task 4: Display account information for each account
account1.display_account_info()
account2.display_account_info()
