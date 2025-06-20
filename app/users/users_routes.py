from fastapi import APIRouter

from app.users.users_db_queries import db_insert_user, db_select_user, db_select_all_users, db_delete_user, \
    db_update_user_name, db_update_user_phone_number, db_update_user_email
from app.users.users_shemas import InsertUser

router = APIRouter(
    prefix='/users',
    tags=['Пользователи']
)


@router.post('/insert_user', summary='Добавить пользователя')
def insert_user(requests: InsertUser):
    user = db_insert_user(requests)
    return user


@router.get('/select_user', summary='Запросить пользователя')
def select_user(select_user_name):
    select_user_result = db_select_user(select_user_name)
    return select_user_result


@router.get('/select_all_users', summary='Запросить всех пользователей')
def select_all_users():
    select_all_users_result = db_select_all_users()
    return select_all_users_result


@router.delete('/delete_user', summary='Удалить пользователя')
def delete_user(delete_user_name):
    delete_user_result = db_delete_user(delete_user_name)
    return delete_user_result


@router.put('/update_user_name', summary='Изменить имя пользователя')
def update_user_name(user_name, new_user_name):
    update_user_name_result = db_update_user_name(user_name, new_user_name)
    return update_user_name_result


@router.put('/update_user_phone_number', summary='Изменить номер телефона')
def update_user_phone_number(user_name, new_phone_number):
    update_user_phone_number_result = db_update_user_phone_number(user_name, new_phone_number)
    return update_user_phone_number_result


@router.put('/update_user_email', summary='Изменить email пользователя')
def update_user_email(user_name, new_email):
    update_user_email_result = db_update_user_email(user_name, new_email)
    return update_user_email_result
