# this is a Class which consists of all the functionality related to the bank account
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
        self.transaction_history = []
    # this function is used to deposit money to the bank account
    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposit: +${amount}")
    # this function is used to withdraw money from the bank account
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: -${amount}")
        else:
            print("Insufficient funds. Withdrawal canceled.")
    # this function is used to check the current balance in the bank account
    def check_balance(self):
        print(f"Account Balance for {self.account_holder}: ${self.balance}")
    # this function is used to s
    def display_transaction_history(self):
        print(f"Transaction History for {self.account_holder}:")
        for transaction in self.transaction_history:
            print(transaction)
# this is the main function which will start the banking system from here
def main():
    print("Welcome to the Bank Account System!")

    # Create a new account
    account_holder_name = input("Enter your name: ")
    initial_balance = float(input("Enter initial balance: "))
    user_account = BankAccount(account_holder_name, initial_balance)

    while True:
        print("\nOptions:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Display Transaction History")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            deposit_amount = float(input("Enter deposit amount: "))
            user_account.deposit(deposit_amount)
        elif choice == "2":
            withdrawal_amount = float(input("Enter withdrawal amount: "))
            user_account.withdraw(withdrawal_amount)
        elif choice == "3":
            user_account.check_balance()
        elif choice == "4":
            user_account.display_transaction_history()
        elif choice == "5":
            print("Exiting the Bank Account System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
