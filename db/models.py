from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from db.engine import Base


class DBCheeseType(Base):
    __tablename__ = 'cheese_type'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String(499), nullable=False)
