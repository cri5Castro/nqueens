from datetime import datetime
from sqlalchemy import Column, Sequence,Integer, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import postgresql

Base = declarative_base()


class Solution(Base):
    __tablename__ = 'solution'
    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    n = Column(Integer)
    solution = Column(postgresql.ARRAY(Boolean, dimensions=1))
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return f"** solution({self.id}) **"