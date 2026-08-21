from sqlalchemy import String, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from database.connection import Base

class Professor(Base):
    __tablename__ = 'professores'