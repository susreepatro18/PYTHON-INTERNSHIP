class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.balance

# Main code for testing
if __name__ == "__main__":
    # Create a new BankAccount object
    account = BankAccount("123456789", "John Doe", 1000.0)

    # Display the current balance
    print("Current balance:", account.get_balance())

    # Deposit money
    account.deposit(500.0)
    print("Balance after deposit:", account.get_balance())

    # Withdraw money
    account.withdraw(200.0)
    print("Balance after withdrawal:", account.get_balance())

    # Attempt to withdraw more money than the current balance
    account.withdraw(1500.0)

    # Display the final balance
    print("Final balance:", account.get_balance())
