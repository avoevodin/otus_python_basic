from typing import TYPE_CHECKING

from sqlalchemy import Column, String, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base
from .mixins import TimestampMixin

if TYPE_CHECKING:
    from .user import User


class Post(TimestampMixin, Base):
    """
    The model of post with users model relation.
    """

    title = Column(String(200), nullable=False)
    body = Column(Text, nullable=False, default="", server_default="")

    user_id = Column(Integer, ForeignKey("users.id"), unique=False, nullable=False)
    user = relationship("User", back_populates="posts")

    if TYPE_CHECKING:
        user: User

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}"
            f", title={self.title}"
            f", user_id={self.user_id}"
            f", created_at={self.created_at}"
            ")"
        )
