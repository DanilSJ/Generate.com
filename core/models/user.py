from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from .base import Base


class User(Base):
    username: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String)
