import uvicorn
from fastapi import FastAPI

from storage.database import engine
from storage.models import Base
from app.users.users_routes import router as user_router
from app.bank_accounts.bank_accounts_routes import router as bank_accounts_router
from app.transactions.transactions_routes import router as transaction_router

# Base.metadata.drop_all(bind=engine, checkfirst=True)

app = FastAPI(
    title='Банковское приложение'
)


@app.get('/home_page', summary='Главная страница', tags=['Основные'])
def home_page():
    return f'Добро пожаловать на сайт!'


app.include_router(user_router)
app.include_router(bank_accounts_router)
app.include_router(transaction_router)


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=9000)
