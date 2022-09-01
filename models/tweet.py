#Python
from datetime import datetime
from uuid import UUID
from typing import Optional

#Pydantic
from pydantic import BaseModel
from pydantic import Field

#models
from users import User


class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ..., 
        min_length=1, 
        max_length=256
    )
    created_at: datetime = Field(default=datetime.now())
    update_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)
