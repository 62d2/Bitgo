from typing import List, Optional

from sqlmodel import SQLModel, Field


class EmailNoticeLog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    from_email: str
    to_emails: List[str]
    bcc_emails: List[str]
    subject: str
    content: str
    notice_log_id: int
    status: str  # enum : created, send, failed
    retry_attempt: int = Field(default=0)
