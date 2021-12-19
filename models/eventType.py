"""Model oof the user
    """
from sqlalchemy import String, Integer, ForeignKey, Column

from config import Base


class EventType(Base):
    """EventType Schema"""

    __tablename__ = 'event_type'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
