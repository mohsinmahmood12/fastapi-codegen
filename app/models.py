from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class CodeRequest(BaseModel):
    description: str

class FeedbackRequest(BaseModel):
    feedback: str

class CodeSnippet(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    code: str
    created_at: datetime = Field(default_factory=datetime.now)