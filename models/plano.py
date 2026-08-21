from decimal import Decimal
from sqlalchemy import String, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from database.connection import Base

class Plano(Base):
    __tablename__ = 'planos'

    id: Mapped[int] = mapped_column(primary_key=True)
    nome_plano: Mapped[str] = mapped_column(String(100), nullable=False)
    valor: Mapped[Decimal] = mapped_column((10, 2), nullable=False)
