from uuid import UUID
from enums.transaction_type import TransactionType
from infrastructure.account_repository import AccountRepository


class TransactionUseCase:
    def __init__(self, account_repository):
        self.account_repository: AccountRepository = account_repository

    def make_transaction(
        self, account_id: UUID, amount: int, transaction_type: TransactionType
    ):
        try:
            account = self.account_repository.find_account_by_id(account_id)

            if transaction_type == TransactionType.DEPOSIT:
                account.deposit(amount)
            elif transaction_type == TransactionType.WITHDRAW:
                account.withdraw(amount)

            self.account_repository.save_account(account)

        except ValueError as e:
            print(e)
