from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ActivityBase(BaseModel):
    name: str
    description: Optional[str] = None
    duration: int
    distance: float
    avg_heart_rate: Optional[int] = None


class ActivityCreate(ActivityBase):
    pass


class ActivityUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    duration: Optional[int] = None
    distance: Optional[float] = None
    avg_heart_rate: Optional[int] = None


class ActivityInDB(ActivityBase):
    id: int
    start_time: datetime

    class Config:
        orm_mode = True
