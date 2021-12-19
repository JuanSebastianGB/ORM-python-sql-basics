"""Model oof the user
    """
from sqlalchemy import String, Integer, ForeignKey, Column, Date

from config import Base


class Event(Base):
    """Event Schema"""

    __tablename__ = 'event'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    date = Column(Date, nullable=False)
    attendees = Column(Integer, nullable=False, default=0)

    created_by = Column(Integer, ForeignKey('user.id'), nullable=False)
    type = Column(Integer, ForeignKey('event_type.id'), nullable=False)
