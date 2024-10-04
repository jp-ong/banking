from uuid import UUID
from domain.entities.account import Account
from infrastructure.account_repository import AccountRepository


class AccountUseCase:
    def __init__(self, account_repository):
        self.account_repository: AccountRepository = account_repository

    def create_account(self, customer_id: UUID, account_number: int) -> Account:
        account = Account(
            customer_id=customer_id, account_number=account_number, balance=0
        )
        self.account_repository.save_account(account)
        return account
