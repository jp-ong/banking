from typing import List
from uuid import UUID
from domain.entities.account import Account


class AccountRepository:
    def __init__(self):
        self.accounts = {}

    def save_account(self, account: Account):
        self.accounts[account.account_id] = account

    def find_account_by_id(self, account_id: UUID) -> Account | None:
        return self.accounts.get(account_id)

    def find_accounts_by_customer_id(self, customer_id: UUID) -> List[Account]:
        return [
            account
            for account in self.accounts.values()
            if account.customer_id == customer_id
        ]
