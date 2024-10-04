from uuid import UUID, uuid4


class Account:
    def __init__(self, customer_id: UUID, account_number: int, balance: int = 0):
        self.account_id = uuid4()
        self.customer_id = customer_id
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount: int):
        if amount < 0:
            raise ValueError("Invalid deposit amount")
        self.balance += amount

    def withdraw(self, amount: int):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount

    def get_balance(self):
        return self.balance
