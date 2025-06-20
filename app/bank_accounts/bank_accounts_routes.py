from fastapi import APIRouter

from app.bank_accounts.bank_accounts_db_queries import db_insert_user_bank_account, db_select_user_bank_account, \
    db_select_all_bank_accounts, db_delete_user_bank_account, db_delete_all_user_bank_accounts, \
    db_select_all_user_bank_accounts, db_update_user_amount_of_money

router = APIRouter(
    prefix='/bank_accounts',
    tags=['Банковские счета']
)


@router.post('/insert_user_bank_account', summary='Добавить счет')
def insert_user_bank_account(user_name, amount_of_money):
    bank_account = db_insert_user_bank_account(user_name, amount_of_money)
    return bank_account


@router.get('/select_user_bank_account', summary='Запроить счет')
def select_user_bank_account(user_name):
    select_user_bank_account_result = db_select_user_bank_account(user_name)
    return select_user_bank_account_result


# @router.get('/select_all_user_bank_accounts', summary='Запросить все счета пользователя')
# def select_all_user_bank_accounts(user_name):
#     select_all_user_bank_accounts_result = db_select_all_user_bank_accounts(user_name)
#     return select_all_user_bank_accounts_result


@router.get('/select_all_bank_accounts', summary='Запросить все счета')
def select_all_bank_accounts():
    select_all_bank_accounts_result = db_select_all_bank_accounts()
    return select_all_bank_accounts_result


@router.delete('/delete_user_bank_account', summary='Удалить счет')
def delete_user_bank_account(user_name):
    delete_user_bank_account_result = db_delete_user_bank_account(user_name)
    return delete_user_bank_account_result


# @router.delete('/delete_all_user_bank_accounts', summary='Удалить все счета пользователя')
# def delete_all_user_bank_accounts(user_name):
#     delete_all_user_bank_accounts_result = db_delete_all_user_bank_accounts(user_name)
#     return delete_all_user_bank_accounts_result


@router.put('/update_user_amount_of_money', summary='Изменить количество средств на счету')
def update_user_amount_of_money(user_name, new_amount_of_money):
    update_user_amount_of_money_result = db_update_user_amount_of_money(user_name, new_amount_of_money)
    return update_user_amount_of_money_result
