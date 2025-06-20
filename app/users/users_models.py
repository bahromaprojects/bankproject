from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from storage.models import Base, an_uuid_primary_key


class Users(Base):
    __tablename__: str = 'users'
    user_id: Mapped[an_uuid_primary_key]
    user_name: Mapped[str] = mapped_column(nullable=False, unique=True)
    user_phone_number: Mapped[str] = mapped_column(String(11), nullable=False, unique=True)
    user_email: Mapped[str] = mapped_column(unique=True, nullable=False)

    def __init__(self, user_name, user_phone_number, user_email):
        self.user_name = user_name
        self.user_phone_number = user_phone_number
        self.user_email = user_email
