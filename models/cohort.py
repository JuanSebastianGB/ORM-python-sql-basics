"""Model oof the user
    """
from sqlalchemy import String, Integer, ForeignKey, Column

from config import Base


class Cohort(Base):
    """Cohort Schema"""

    __tablename__ = 'cohort'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
