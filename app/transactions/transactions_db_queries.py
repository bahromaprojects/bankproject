from app.bank_accounts.bank_accounts_models import BankAccounts
from app.transactions.transactions_models import Transactions
from app.users.users_models import Users
from storage.database import session_factory


def db_insert_transaction(user_name, recipient_name, amount):
    amount = int(amount)
    with session_factory() as session:
        user = session.query(Users).filter(Users.user_name == user_name).first()
        if user is None:
            return f'Пользователь {user_name} не найден.'
        user_id = user.user_id
        account = session.query(BankAccounts).filter(BankAccounts.user_id == user_id).first()
        if account is None:
            return f'Счет пользователя {user_name} не найден.'
        if account.amount_of_money < amount:
            return f'Недостаточно средств на счете пользователя {user_name}'
        account.amount_of_money = account.amount_of_money - amount
        account_id = account.account_id
        recipient = session.query(Users).filter(Users.user_name == recipient_name).first()
        if recipient is None:
            return f'Пользователь {recipient_name} не найден.'
        recipient_id = recipient.user_id
        recipient_account = session.query(BankAccounts).filter(BankAccounts.user_id == recipient_id).first()
        if recipient_account is None:
            return f'Счет пользователя {recipient_name} не найден.'
        recipient_account.amount_of_money = recipient_account.amount_of_money + amount
        recipient_account_id = recipient_account.account_id
        transaction = Transactions(user_id, account_id, recipient_id, recipient_account_id, amount)
        session.add(transaction)
        session.commit()
    return f'Перевод успешно обработан.'
