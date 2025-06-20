from sqlalchemy import UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from storage.models import Base, an_uuid_primary_key, an_created_at


class Transactions(Base):
    __tablename__: str = 'transactions'
    transaction_id: Mapped[an_uuid_primary_key]
    user_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('users.user_id', ondelete='CASCADE'))
    account_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('bank_accounts.account_id', ondelete='CASCADE'))
    created_at: Mapped[an_created_at]
    recipient_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('users.user_id', ondelete='Null'))
    recipient_account_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('bank_accounts.account_id', ondelete='Null'))
    amount: Mapped[int] = mapped_column(default=0)

    def __init__(self, user_id, account_id, recipient_id, recipient_account_id, amount):
        self.user_id = user_id
        self.account_id = account_id
        self.recipient_id = recipient_id
        self.recipient_account_id = recipient_account_id
        self.amount = amount
