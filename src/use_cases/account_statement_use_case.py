from uuid import UUID

from infrastructure.account_repository import AccountRepository


class AccountStatementUseCase:
    def __init__(self, account_repository):
        self.account_repository: AccountRepository = account_repository

    def generate_account_statement(self, account_id: UUID) -> str:
        try:
            account = self.account_repository.find_account_by_id(account_id=account_id)
            return (
                f"Account: {account.account_number} \nBalance: {account.get_balance()}"
            )
        except ValueError as e:
            return str(e)
