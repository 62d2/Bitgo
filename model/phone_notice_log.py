from typing import Optional

from sqlmodel import SQLModel, Field


class PhoneNoticeLog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    phone_number: str
    subject: str
    content: str
    notice_log_id: int
    status: str  # enum : created, send, failed
    retry_attempt: int = Field(default=0)
