import datetime
import uuid
from typing import Annotated

from sqlalchemy import text, UUID, String
from sqlalchemy.orm import mapped_column, declarative_base, Mapped

Base = declarative_base()

an_uuid_primary_key = Annotated[
    UUID,
    mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
]
an_created_at = Annotated[
    datetime.datetime,
    mapped_column(server_default=text("TIMEZONE('utc', now())"))
]


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
