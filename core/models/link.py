from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer
from .base import Base


class Link(Base):
    old: Mapped[str] = mapped_column(String)
    new: Mapped[str] = mapped_column(String)
    click_count: Mapped[int] = mapped_column(Integer, default=0, nullable=True)
