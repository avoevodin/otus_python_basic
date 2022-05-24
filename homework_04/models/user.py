from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from typing import TYPE_CHECKING, List

from .base import Base
from .mixins import TimestampMixin

if TYPE_CHECKING:
    from .post import Post


class User(TimestampMixin, Base):
    """
    The model of user with posts model relation.
    """

    name = Column(String(100), unique=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(80), unique=True, nullable=False)

    posts = relationship("Post", back_populates="user")

    if TYPE_CHECKING:
        posts: List[Post]

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}"
            f", name={self.name}"
            f", username={self.username}"
            f", email={self.email}"
            f", created_at={self.created_at}"
            ")"
        )
