import datetime

from models.base import Base
from sqlalchemy import Column, DateTime, Float, Integer, String


class Activity(Base):
    __table__ = 'activities'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    start_time = Column(DateTime, default=datetime.datetime.utcnow())
    duration = Column(Integer, nullable=False) # In minutes
    distance = Column(Float, nullable=False)
    avg_heart_rate = Column(Integer, nullable=True)
