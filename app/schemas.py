from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional


class IssueStatus(str, Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    CLOSED = "closed"


class IssuePriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class IssueCreate(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(min_length=5, max_length=1000)
    priority: IssuePriority = IssuePriority.MEDIUM  # default


class IssueUpdate(BaseModel):
    title: Optional[str] = Field(default=None, max_length=100)  # basically null is JS
