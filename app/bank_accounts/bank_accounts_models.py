from typing import Annotated

from sqlalchemy import UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from storage.models import Base, an_uuid_primary_key, an_created_at

an_uuid_foreign_key = Annotated[
    UUID,
    mapped_column(UUID(as_uuid=True), ForeignKey('users.user_id', ondelete='CASCADE'))
]


class BankAccounts(Base):
    __tablename__: str = 'bank_accounts'
    account_id: Mapped[an_uuid_primary_key]
    amount_of_money: Mapped[int] = mapped_column(default=0)
    user_id: Mapped[an_uuid_foreign_key]
    created_at: Mapped[an_created_at]

    def __init__(self, amount_of_money, user_id):
        self.amount_of_money = amount_of_money
        self.user_id = user_id
