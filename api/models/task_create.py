from pydantic import BaseModel
from typing import List, Optional
from datetime import date, datetime


class TaskCreate(BaseModel):
    content: str
    description: Optional[str] = None
    project_id: Optional[str] = None
    section_id: Optional[str] = None
    parent_id: Optional[str] = None
    order: Optional[int] = None
    labels: Optional[List[str]] = []
    priority: Optional[int] = 0
    assignee_id: Optional[int] = None
    due_string: Optional[str] = None
    due_date: Optional[date] = None
    due_datetime: Optional[datetime] = None
    due_lang: Optional[str] = None
    duration: Optional[int] = None
    duration_unit: Optional[str] = None
    deadline_date: Optional[date] = None
    deadline_lang: Optional[str] = None
