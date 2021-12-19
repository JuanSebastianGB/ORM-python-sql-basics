"""Model oof the user
    """
from sqlalchemy import String, Integer, ForeignKey, Column
from sqlalchemy.orm import relationship
from models.event import Event

from config import Base


class User(Base):
    """User Schema"""

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    company = Column(String(100), nullable=False)

    events = relationship('Event', backref='user', cascade='all, delete')
