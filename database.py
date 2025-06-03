import datetime
from typing import Annotated

from sqlalchemy import create_engine, ForeignKey, text, String
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column

engine = create_engine(
    url='postgresql+psycopg://postgres:4568123497@localhost:5432/bank_project',
    echo=False,
)


class Base(DeclarativeBase):
    pass


an_int_primary_key = Annotated[int, mapped_column(primary_key=True)]
an_created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]


class Users(Base):
    __tablename__: str = 'users'
    user_id: Mapped[an_int_primary_key]
    user_name: Mapped[str] = mapped_column(nullable=False)
    user_phone_number: Mapped[str] = mapped_column(String(11), nullable=False, unique=True)
    user_email: Mapped[str] = mapped_column(unique=True, nullable=False)

    def __init__(self, user_name, user_phone_number, user_email, **kw):
        super().__init__(**kw)
        self.user_name = user_name
        self.user_phone_number = user_phone_number
        self.user_email = user_email

    @staticmethod
    def insert_user(user_name, user_phone_number, user_email):
        user = Users(user_name, user_phone_number, user_email)
        with session_factory() as session:
            session.add(user)
        return f'Пользователь добавлен {user_name}, {user_phone_number}, {user_email}'


class BankAccounts(Base):
    __tablename__: str = 'bank_accounts'
    account_id: Mapped[an_int_primary_key] = mapped_column(primary_key=True)
    amount_of_money: Mapped[int] = mapped_column(default=0)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id', ondelete='CASCADE'))
    created_at: Mapped[an_created_at]

    def __init__(self, amount_of_money, **kw):
        super().__init__(**kw)
        self.amount_of_money = amount_of_money

    @staticmethod
    def insert_bank_account(amount_of_money):
        bank_account = BankAccounts(amount_of_money)
        with session_factory() as session:
            session.add(bank_account)


session_factory = sessionmaker()

# with engine.connect() as connection:
#     result = connection.execute("SELECT version();")
#     version = result.fetchone()
#     print(f"PostgreSQL version: {version[0]}")

# Base.metadata.create_all(engine)

try:
    with engine.connect() as connection:
        result = connection.execute("SELECT version();")
        version = result.fetchone()
        print(f"PostgreSQL version: {version[0]}")
except Exception as e:
    print(f"Ошибка подключения: {e}")


