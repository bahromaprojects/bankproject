import uvicorn
from fastapi import FastAPI

from database import Users, BankAccounts

app = FastAPI(
    title='Bank APP'
)


@app.get('/{add_user}', summary='Добавить пользователя')
def add_user(user_name, user_phone_number, user_email):
    Users.insert_user(user_name, user_phone_number, user_email)


@app.get('/{add_bank_account}', summary='Добавить счет')
def add_bank_account(amount_of_money):
    BankAccounts.insert_bank_account(amount_of_money)


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=9000)


