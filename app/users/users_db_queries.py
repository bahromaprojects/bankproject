from app.users.users_shemas import InsertUser
from storage.database import session_factory, engine
from storage.models import Base
from app.users.users_models import Users


def db_insert_user(requests: InsertUser):
    user = Users(requests.user_name, requests.user_phone_number, requests.user_email)
    with session_factory() as session:
        session.add(user)
        session.commit()
    return f'Пользователь {requests.user_name} успешно добавлен.'


def db_select_user(user_name):
    with session_factory() as session:
        user = session.query(Users).filter(Users.user_name == user_name).first()
    if user is None:
        return f'Пользователь {user_name} не найден.'
    return user


def db_select_all_users():
    with session_factory() as session:
        users = session.query(Users).all()
    if users is None:
        return f'Пользователи не найдены.'
    return users


def db_delete_user(user_name):
    with session_factory() as session:
        user = session.query(Users).filter(Users.user_name == user_name).first()
        if user is None:
            return f'Пользователь {user_name} не найден.'
        session.delete(user)
        session.commit()
    return f'Пользователь {user_name} успешно удален.'


def db_update_user_name(user_name, new_user_name):
    with session_factory() as session:
        user = session.query(Users).filter(Users.user_name == user_name).first()
        if user is None:
            return f'Пользователь {user_name} не найден.'
        user.user_name = new_user_name
        session.commit()
    return f'Пользователь {user_name} успешно изменил имя на {new_user_name}.'


def db_update_user_phone_number(user_name, new_phone_number):
    with session_factory() as session:
        user = session.query(Users).filter(Users.user_name == user_name).first()
        if user is None:
            return f'Пользователь {user_name} не найден.'
        user.user_phone_number = new_phone_number
        session.commit()
    return f'Пользователь {user_name} успешно изменил номер на {new_phone_number}.'


def db_update_user_email(user_name, new_email):
    with session_factory() as session:
        user = session.query(Users).filter(Users.user_name == user_name).first()
        if user is None:
            return f'Пользователь {user_name} не найден.'
        user.user_email = new_email
        session.commit()
    return f'Пользователь {user_name} успешно изменил email на {new_email}.'


def db_create_table_users():
    Base.metadata.create_all(bind=engine, tables=[Users.__table__], checkfirst=True)


def db_drop_table_users():
    Base.metadata.drop_all(bind=engine, tables=[Users.__table__], checkfirst=True)
