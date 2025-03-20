import logging

# Configure logging to write to 'bank.log'
logging.basicConfig(
    filename="bank.log",
    level=logging.DEBUG,
    format='%(levelname)s - %(message)s'
)

class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        """
        Initializes a new BankAccount instance.

        :param account_holder: Name of the account holder (string)
        :param balance: Initial balance (float), defaults to 0.0
        """
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        :param amount: The amount to deposit (float)
        :raises ValueError: If amount is negative
        """
        if amount < 0:
            logging.error(f"Invalid deposit amount: ${amount}")
            raise ValueError("Deposit amount cannot be negative.")
        if amount == 0:
            # Deposit of 0 is allowed, but doesn't change balance
            logging.info(f"Deposit of $0 did not change balance. Current Balance: ${self.balance}")
            return
        self.balance += amount
        logging.info(f"Deposit: ${amount} | New Balance: ${self.balance}")

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account.

        :param amount: The amount to withdraw (float)
        :raises ValueError: If amount is negative or exceeds current balance
        """
        if amount < 0:
            logging.error(f"Invalid withdrawal amount: ${amount}")
            raise ValueError("Withdrawal amount cannot be negative.")
        if amount > self.balance:
            logging.warning(f"Insufficient funds for withdrawal: ${amount}")
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        logging.info(f"Withdrawal: ${amount} | New Balance: ${self.balance}")

    def get_balance(self):
        """
        Returns the current balance of the account.

        :return: The current balance (float)
        """
        return self.balance


if __name__ == "__main__":
     account = BankAccount("Alice", 1000)
     print("Initial Balance:", account.get_balance())
     account.deposit(500)
     print("After depositing $500:", account.get_balance())
     try:
         account.deposit(-50)
     except ValueError as e:
         print("Error on deposit:", e)
     account.withdraw(200)
     print("After withdrawing $200:", account.get_balance())
     try:
         account.withdraw(2000)
     except ValueError as e:
         print("Error on withdrawal:", e)
     balance_before = account.get_balance()
     account.deposit(0)
     print("After depositing $0 (balance unchanged):", account.get_balance())
     account.withdraw(account.get_balance())
     print("After withdrawing the exact balance (should be 0):", account.get_balance())
     print("Check 'bank.log' for logged transaction details.")
