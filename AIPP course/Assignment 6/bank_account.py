class BankAccount:
    """A simple BankAccount class with deposit, withdraw, and balance methods."""
    
    def __init__(self, initial_balance=0.0):
        self._balance = initial_balance
    
    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self._balance += amount
            print(f"Deposited: {int(amount)}, New Balance: {int(self._balance)}")
            return True
        return False
    
    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew: {int(amount)}, Remaining Balance: {int(self._balance)}")
            return True
        return False
    
    def balance(self):
        """Get the current balance."""
        return self._balance


def main():
    """Test the BankAccount class with user input."""
    try:
        account = BankAccount(float(input("Enter initial balance: ") or 0))
    except:
        account = BankAccount(0)
    
    while True:
        choice = input("\n1. Deposit  2. Withdraw  3. Exit: ")
        if choice == "1":
            try:
                account.deposit(float(input("Deposit amount: ")))
            except:
                pass
        elif choice == "2":
            try:
                account.withdraw(float(input("Withdraw amount: ")))
            except:
                pass
        elif choice == "3":
            print(f"Final Balance: {int(account.balance())}")
            break


if __name__ == "__main__":
    main()
