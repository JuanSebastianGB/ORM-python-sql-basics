"""Model oof the user
    """
from sqlalchemy import String, Integer, ForeignKey, Column

from config import Base


class Campus(Base):
    """Campus Schema"""

    __tablename__ = 'campus'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
