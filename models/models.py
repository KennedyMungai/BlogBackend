"""The file that holds the models logic"""
from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.db import Base


class User(Base):
    """The model for the user data

    Args:
        Base (Db Base): The database base class
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=True)

    articles = relationship(
        "Article", back_populates="author", cascade="all,delete")


class Article(Base):
    """The article model

    Args:
        Base (Db base): The database thing
    """
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True)
    body = Column(String(255))
    created_at = Column(DateTime(), default=datetime.now())
    updated_at = Column(DateTime(), onupdate=datetime.now())
    author_id = Column(Integer, ForeignKey("users.id"),
                       nullable=False, ondelete="CASCADE")
