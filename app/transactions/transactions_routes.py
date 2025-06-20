from fastapi import APIRouter

from app.transactions.transactions_db_queries import db_insert_transaction

router = APIRouter(
    prefix='/transactions',
    tags=['Переводы']
)


@router.post('/insert_transaction', summary='Добавить транзакцию')
def insert_transaction(user_name, recipient_name, amount):
    insert_transaction_result = db_insert_transaction(user_name, recipient_name, amount)
    return insert_transaction_result
