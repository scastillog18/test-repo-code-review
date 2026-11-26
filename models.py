from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


VALID_STATUSES = {"open", "in_progress", "done"}


@dataclass
class User:
    id: Optional[int]
    name: str
    email: str
    created_at: Optional[datetime] = None

    def validate(self) -> list[str]:
        errors = []
        if not self.name or not self.name.strip():
            errors.append("name is required")
        if not self.email or "@" not in self.email:
            errors.append("valid email is required")
        return errors


@dataclass
class Task:
    id: Optional[int]
    title: str
    description: str = ""
    status: str = "open"
    owner_id: Optional[int] = None
    created_at: Optional[datetime] = None

    def validate(self) -> list[str]:
        errors = []
        if not self.title or not self.title.strip():
            errors.append("title is required")
        if self.status not in VALID_STATUSES:
            errors.append(f"status must be one of {VALID_STATUSES}")
        return errors
