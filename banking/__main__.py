from banking.domain.entities.customer import Customer
from banking.enums.transaction_type import TransactionType
from banking.infrastructure.account_repository import AccountRepository
from banking.use_cases.account_statement_use_case import AccountStatementUseCase
from banking.use_cases.account_use_case import AccountUseCase
from banking.use_cases.transaction_use_case import TransactionUseCase


def main():
    # Infrastructure (repository setup)
    account_repository = AccountRepository()

    # Use cases
    account_use_case = AccountUseCase(account_repository)
    transaction_use_case = TransactionUseCase(account_repository)
    account_statement_use_case = AccountStatementUseCase(account_repository)

    # Create a customer and account
    customer = Customer(
        name="John Paul Ong", email="jpong5202@gmail.com", phone_number=9173243289
    )
    account = account_use_case.create_account(
        customer_id=customer.customer_id, account_number=123456789
    )
    statement = account_statement_use_case.generate_account_statement(
        account_id=account.account_id
    )
    print(statement)
    print("")

    # Initial Deposit
    print("[Transaction] DEPOSIT: 50000")
    transaction_use_case.make_transaction(
        account_id=account.account_id,
        amount=50000,
        transaction_type=TransactionType.DEPOSIT,
    )
    statement = account_statement_use_case.generate_account_statement(
        account_id=account.account_id
    )
    print(statement)
    print("")

    # Valid Withdraw
    print("[Transaction] WITHDRAW: 7500")
    transaction_use_case.make_transaction(
        account_id=account.account_id,
        amount=7500,
        transaction_type=TransactionType.WITHDRAW,
    )
    statement = account_statement_use_case.generate_account_statement(
        account_id=account.account_id
    )
    print(statement)
    print("")

    # Invalid Withdraw
    print("[Transaction] WITHDRAW: 100000")
    transaction_use_case.make_transaction(
        account_id=account.account_id,
        amount=100000,
        transaction_type=TransactionType.WITHDRAW,
    )
    statement = account_statement_use_case.generate_account_statement(
        account_id=account.account_id
    )
    print(statement)
    print("")

    # Invalid Deposit
    print("[Transaction] DEPOSIT: -999")
    transaction_use_case.make_transaction(
        account_id=account.account_id,
        amount=-999,
        transaction_type=TransactionType.DEPOSIT,
    )
    statement = account_statement_use_case.generate_account_statement(
        account_id=account.account_id
    )
    print(statement)
    print("")


if __name__ == "__main__":
    main()
