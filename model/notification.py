import enum
from typing import Optional

from sqlmodel import Field, SQLModel


class NotificationMode(enum):
    Email = "Email"


class Notification(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
    price: float
    market_trade: float
    id_high_price: float
    market_cap: float
    mode: NotificationMode
    attempt: int
    status: str  # enum : created, send, failed
