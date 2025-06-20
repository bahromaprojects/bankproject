from app.bank_accounts.bank_accounts_models import BankAccounts
from app.users.users_models import Users
from storage.database import session_factory


def db_insert_user_bank_account(user_name, amount_of_money):
    with session_factory() as session:
        user = session.query(Users).filter(Users.user_name == user_name).first()
        if user is None:
            return f'Пользователь {user_name} не найден.'
        user_id = user.user_id
        bank_account = BankAccounts(amount_of_money, user_id)
        session.add(bank_account)
        session.commit()
    return f'Счет пользователя {user_name} успешно добавлен.'


def db_select_user_bank_account(user_name):
    with session_factory() as session:
        user = session.query(Users).filter(Users.user_name == user_name).first()
        if user is None:
            return f'Пользователь {user_name} не найден.'
        user_id = user.user_id
        bank_account = session.query(BankAccounts).filter(BankAccounts.user_id == user_id).first()
    if bank_account is None:
        return f'Счет пользователя {user_name} не найден.'
    return bank_account


def db_select_all_user_bank_accounts(user_name):
    with session_factory() as session:
        user = session.query(Users).filter(Users.user_name == user_name).first()
        if user is None:
            return f'Пользователь {user_name} не найден.'
        user_id = user.user_id
        bank_accounts = session.query(BankAccounts).filter(BankAccounts.user_id == user_id).all()
    if bank_accounts is None:
        return f'Счета пользователя {user_name} не найдены.'
    return bank_accounts


def db_select_all_bank_accounts():
    with session_factory() as session:
        bank_accounts = session.query(BankAccounts).all()
    if bank_accounts is None:
        return f'Счета не найдены.'
    return bank_accounts


def db_delete_user_bank_account(user_name):
    with session_factory() as session:
        user = session.query(Users).filter(Users.user_name == user_name).first()
        if user is None:
            return f'Пользователь {user_name} не найден.'
        user_id = user.user_id
        bank_account = session.query(BankAccounts).filter(BankAccounts.user_id == user_id).first()
        if bank_account is None:
            return f'Счет пользователя {user_name} не найден.'
        session.delete(bank_account)
        session.commit()
    return f'Счет пользователя {user_name} успешно удален.'


def db_delete_all_user_bank_accounts(user_name):
    with session_factory() as session:
        user = session.query(Users).filter(Users.user_name == user_name).first()
        if user is None:
            return f'Пользователь {user_name} не найден.'
        user_id = user.user_id
        bank_accounts = session.query(BankAccounts).filter(BankAccounts.user_id == user_id).all()
        if bank_accounts is None:
            return f'Счета пользователя {user_name} не найдены.'
        for bank_account in bank_accounts:
            session.delete(bank_account)
        session.commit()
    return f'Все счета пользователя {user_name} успешно удалены.'


def db_update_user_amount_of_money(user_name, new_amount_of_money):
    with session_factory() as session:
        user = session.query(Users).filter(Users.user_name == user_name).first()
        if user is None:
            return f'Пользователь {user_name} не найден.'
        user_id = user.user_id
        bank_account = session.query(BankAccounts).filter(BankAccounts.user_id == user_id).first()
        if bank_account is None:
            return f'Счет пользователя {user_name} не найден.'
        bank_account.amount_of_money = new_amount_of_money
        session.commit()
    return f'Количество средств на счету пользователя {user_name} успешно изменено на {new_amount_of_money}.'
