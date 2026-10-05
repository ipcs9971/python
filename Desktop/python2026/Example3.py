# Example 3 — Bank Account

# Now let's build a more realistic OOP program.

# Problem

# Create a banking system with:

# Account holder
# Account number
# Balance
# Deposit
# Withdraw
# Check balance


#*********************************************************************************************************

class BankAccount:

    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):

        if amount > 0:
            self.balance = self.balance + amount
            print("Deposit successful")
        else:
            print("Invalid amount")

    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid amount")

        elif amount > self.balance:
            print("Insufficient balance")

        else:
            self.balance = self.balance - amount
            print("Withdrawal successful")

    def check_balance(self):
        print("Account Holder:", self.name)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)


account1 = BankAccount(101, "Rahul", 10000)

account1.check_balance()

account1.deposit(5000)

account1.withdraw(3000)

account1.check_balance()